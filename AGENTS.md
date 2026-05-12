# Ankora-World AI 協作協議

> **版本**：v0.2  
> **用途**：定義 Kimi Code CLI 內部如何透過子代理（subagent）並行工作，同時避免 Codespaces 休眠陷阱。  
> **核心原則**：一個會話 + 多個子代理，而非多個獨立進程。

---

## 一、重要警告：Codespaces 休眠機制

GitHub Codespaces 的休眠判定依據是**鍵盤/滑鼠活動**，而非 CPU 使用率。

| 情境 | 結果 |
|------|------|
| 你在 VS Code 側邊欄和我對話 | ✅ Codespaces 認為你在工作，不會休眠 |
| 你跑去睡覺，終端機裡的 `kimi` 還在跑 | ❌ Codespaces 30 分鐘後直接休眠，進程被殺 |
| 你同時開兩個 `kimi` 會話 | ❌ 兩個都會在休眠時被殺，且彼此無法通信 |

**結論**：不要依賴終端機裡的獨立 `kimi` 進程做長時間後台工作。所有任務應該在我（當前會話）內部透過子代理完成。

---

## 二、正確的並行工作模式：Subagent 而非獨立進程

Kimi Code CLI 支援在一個會話內啟動多個 **subagent（子代理）** 並行處理不同任務。這和「終端機開另一個 `kimi`」的差別：

| 特性 | 子代理（Subagent） | 獨立進程（`kimi -r`） |
|------|-------------------|----------------------|
| 共享上下文 | ✅ 統一 approval runtime | ❌ 完全隔離 |
| 並行數量 | 最多 30 個同時請求 | 取決於機器資源 |
| Codespaces 休眠 | ✅ 不影響（主會話活躍） | ❌ 休眠時被殺 |
| 任務邊界 | 清晰（由父代理分配） | 模糊（各自為政） |
| 結果彙整 | 父代理自動收集 | 需手動合併 |

**推薦做法**：所有並行任務都在當前會話內透過子代理完成。

---

## 三、任務邊界劃分協議

當需要並行處理時，父代理（我）會：

1. **列出清晰的並排任務清單**（如下格式）
2. **為每個子代理寫入獨立的臨時任務檔案**（`tasks/{agent_name}.md`）
3. **啟動子代理並行執行**
4. **收集結果並彙整**

### 3.1 並排任務清單格式

```markdown
## 批次任務：Batch 1 — 地理實體 YAML

| # | 子代理 | 任務 | 輸入 | 輸出 | 預估時間 |
|---|--------|------|------|------|---------|
| 1 | geo-agent-1 | 建立怒嘯山脈 YAML | source/ 序章 + SCHEMA.md | data/01-west-seraphion/locations/the-howling-peaks.yaml | 10 min |
| 2 | geo-agent-2 | 建立阿比蘇斯深淵 YAML | source/ 序章 + SCHEMA.md | data/01-west-seraphion/locations/the-abyssus.yaml | 10 min |
| 3 | geo-agent-3 | 建立艾爾達拉世界樹 YAML | source/ 序章 + SCHEMA.md | data/05-secret-eldara/locations/eldara-worldtree.yaml | 10 min |
```

### 3.2 子代理臨時任務檔案

每個子代理啟動前，父代理會寫入：

```
tasks/
├── geo-agent-1.md          # 子代理 1 的任務書
├── geo-agent-2.md
└── geo-agent-3.md
```

任務書內容必須包含：
- 目標檔案路徑
- SCHEMA.md 的相關章節
- source/ 原文的參考段落（行號或關鍵字）
- 已知的 `parent_id` 與 `connections`
- 任何需要推斷（inferred）的項目清單

### 3.3 子代理的權限邊界

| 允許 | 禁止 |
|------|------|
| 讀取 `source/`、`SCHEMA.md`、已存在的 YAML 範本 | 修改 `SCHEMA.md` 或 `schema.json` |
| 在指定的輸出路徑寫入 YAML | 創建新的目錄層級（需父代理同意） |
| 讀取其他子代理已完成的 YAML（若需交叉引用） | 修改其他子代理正在寫入的檔案 |
| 在任務檔案中記錄問題或假設 | 直接 `git commit`（由父代理統一處理） |

---

## 四、上下文恢復流程（Context Recovery）

無論是父代理還是子代理，啟動時的標準動作：

1. 讀取 `PLAN.md` → 理解整體藍圖
2. 讀取 `SCHEMA.md` → 確認當前 schema 版本
3. 讀取 `TASKLOG.md` → 檢查最近進展與阻擋問題
4. 讀取 `git log --oneline -10` → 確認提交歷史
5. 掃描 `data/` 下的 YAML 數量與結構 → 評估完成度

> **子代理額外動作**：讀取自己的 `tasks/{agent_name}.md` 任務書。

---

## 五、任務狀態板（Living Status Board）

本區塊由父代理在每次重大進展後更新。

| 模組 | 狀態 | 備註 |
|------|------|------|
| 目錄結構 | ✅ 完成 | `data/`, `api/`, `site/`, `source/` 已建立 |
| SCHEMA.md | ✅ 完成 | v0.1，含 `geography` 層級 |
| schema.json | ✅ 完成 | v0.1，機器可驗證 |
| data/index.yaml | ✅ 完成 | 五大區域 + 秘境索引 |
| PLAN.md | ✅ 完成 | 可見於根目錄 |
| AGENTS.md | ✅ 完成 | v0.2，定義子代理協作協議 |
| FastAPI 骨架 | ⬜ 未開始 | 待 schema 穩定後建立 |
| 示範地點 YAML | ⬜ 未開始 | 等待批次任務指派 |
| 地理實體 YAML | ⬜ 未開始 | Batch 1 待定 |
| 文本批次提取 | ⬜ 未開始 | Batch 1~4 待定 |
| 圖譜層 (Kuzu) | ⬜ 未開始 | 未來擴展 |
| 視覺化前端 | ⬜ 未開始 | 未來擴展 |

---

## 六、常見問答（FAQ for AI）

**Q：為什麼不能用終端機的 `kimi` 跑背景任務？**  
A：Codespaces 會因無鍵盤活動而休眠，殺死所有背景進程。子代理運行在當前活躍會話內，不受影響。

**Q：子代理發現 SCHEMA 有矛盾，怎麼辦？**  
A：子代理在任務檔案中記錄問題，由父代理統一審查並決定是否更新 SCHEMA。

**Q：子代理想新增一個 `layer` 值，怎麼辦？**  
A：禁止自行新增。在任務檔案中提案，父代理審查後統一更新 SCHEMA.md + schema.json。

**Q：子代理的任務衝突了（都想寫同一個檔案），怎麼辦？**  
A：父代理負責任務分配時避免衝突。若發生衝突，後完成的子代理結果覆蓋先完成的，父代理需人工介入審查。

**Q：上下文消失了，怎麼辦？**  
A：根據「上下文恢復流程」重新讀取 `PLAN.md` + `SCHEMA.md` + `TASKLOG.md` + `git log`，即可在 30 秒內恢復。

---

## 七、檔案索引（File Index）

| 檔案 | 用途 | 誰負責更新 |
|------|------|-----------|
| `PLAN.md` | 專案總綱與三階段藍圖 | 父代理 |
| `SCHEMA.md` | YAML 欄位規範（人類可讀） | 父代理 |
| `schema.json` | JSON Schema（機器驗證） | 父代理 |
| `AGENTS.md` | 本文件：子代理協作協議 | 父代理 |
| `TASKLOG.md` | 任務日誌與交接記錄 | 父代理統籌，子代理記錄 |
| `tasks/*.md` | 子代理臨時任務書 | 父代理寫入，子代理讀取 |
| `data/index.yaml` | 大陸與帝國索引 | 父代理 |
| `data/**/*.yaml` | 具體地點資料 | 子代理（在父代理監督下） |
| `api/main.py` | FastAPI 查詢引擎 | 父代理 |
| `source/ankora-chronicles.md` | 原始敘事文本（只讀） | 人類 / 不移動 |

---

## 八、版本歷史

| 版本 | 日期 | 變更 |
|------|------|------|
| v0.1 | 2026-05-12 | 初始版本，錯誤假設為「雙 AI 角色分工」 |
| v0.2 | 2026-05-12 | 修正為「子代理並行協作」，加入 Codespaces 休眠警告與任務邊界協議 |
