# Ankora-World AI 協作協議

> **版本**：v0.1  
> **用途**：解決「上下文消失」問題，讓任何 AI 實例都能在 30 秒內恢復工作狀態。  
> **核心原則**：一切狀態寫入檔案系統，不依賴對話記憶。

---

## 一、雙角色分工

本專案由兩個 AI 角色協作完成。人類可根據任務性質選擇呼叫對象。

### 角色 A：Architect（架構師）

- **載體**：Kimi Code CLI（對話式 AI Agent，可執行 Shell）
- **職責範圍**：
  - 設計與修改 SCHEMA、資料結構、目錄架構
  - 建立骨架程式碼（FastAPI、Pydantic 模型）
  - Git 管理（commit、branch、review）
  - 跨檔案搜尋與重構
  - 審查 Implementer 產出的 YAML/程式碼是否符合 SCHEMA
  - 寫入 PLAN.md、SCHEMA.md、AGENTS.md 等元文件
- **不做的事**：
  - 不逐一手工撰寫大量地點 YAML（這是 Implementer 的工作）
  - 不處理單一檔案內的細微語法修正（交給 Implementer）

### 角色 B：Implementer（實作者）

- **載體**：VS Code Inline Chat / Copilot / 終端機內的 AI 助手
- **職責範圍**：
  - 在已確立的目錄結構內，根據 SCHEMA.md 的規範撰寫具體地點 YAML
  - 從原始文本提取感官細節、歷史事件、關係連結
  - 修改單一檔案內的具體內容（如補全某個房間的 scent）
  - 執行快速測試（curl、uvicorn 啟動）
  - 修復 JSON Schema 驗證錯誤
- **不做的事**：
  - 不創建新的目錄層級（需經 Architect 同意）
  - 不修改 schema.json 或 SCHEMA.md（這是 Architect 的領域）
  - 不執行 Git 變基、強推等危險操作

---

## 二、交接協議（Handoff Protocol）

當一個 AI 的上下文即將消失，或任務需要跨角色協作時，使用以下格式寫入 `TASKLOG.md`：

```markdown
## YYYY-MM-DD HH:MM 交接記錄

- **From**: Architect / Implementer
- **To**: Implementer / Architect
- **任務**：建立聖鑰院複合體 YAML
- **已完成**：
  - [x] 目錄結構 `data/01-west-seraphion/locations/vetustapolis/inner-city/`
  - [x] 從原文提取描述與感官細節
- **待完成**：
  - [ ] 補全 connections（需確認密道 target id）
  - [ ] 補全 events（鐵冠起義年份需 double-check）
- **參考檔案**：`source/ankora-chronicles.md` 第 1452-1489 行
- **阻擋問題**：密道 `papacy_tomb` 的 id 尚未建立，需 Architect 確認命名規範
```

> **規則**：交接記錄必須包含「已完成 / 待完成 / 阻擋問題」三項，缺一不可。

---

## 三、上下文恢復流程（Context Recovery）

無論哪個 AI 被喚醒，第一個動作永遠是「讀取狀態」，而不是「詢問用戶」。

### 3.1 Architect 啟動時

1. 讀取 `PLAN.md` → 理解整體藍圖
2. 讀取 `SCHEMA.md` → 確認當前 schema 版本
3. 讀取 `TASKLOG.md` → 檢查是否有未完成的交接
4. 讀取 `git log --oneline -10` → 確認最近進展
5. 掃描 `data/` 下的 YAML 數量與結構 → 評估完成度

### 3.2 Implementer 啟動時

1. 讀取 `SCHEMA.md` → 確認欄位規範（尤其是 atmosphere 與 connections）
2. 讀取 `data/` 下已存在的黃金範本（如 `sacred-key-complex.yaml`）→ 對齊格式
3. 讀取 `TASKLOG.md` → 檢查被指派的具體任務
4. 讀取 `source/ankora-chronicles.md` 的相關段落 → 提取細節

---

## 四、任務狀態板（Living Status Board）

本區塊由當前工作的 AI 在每次重大進展後更新。用戶可直接查看此處了解進度。

| 模組 | 狀態 | 負責人 | 備註 |
|------|------|--------|------|
| 目錄結構 | ✅ 完成 | Architect | `data/`, `api/`, `site/`, `source/` 已建立 |
| SCHEMA.md | ✅ 完成 | Architect | v0.1，含 `geography` 層級 |
| schema.json | ✅ 完成 | Architect | v0.1，機器可驗證 |
| data/index.yaml | ✅ 完成 | Architect | 五殿 + 秘境索引 |
| PLAN.md | ✅ 完成 | Architect | 可見於根目錄 |
| FastAPI 骨架 | ⬜ 未開始 | Architect | 待 schema 穩定後建立 |
| 示範地點 YAML | ⬜ 未開始 | Implementer | 等待指派 |
| 地理實體 YAML | ⬜ 未開始 | Implementer | 怒嘯山脈、阿比蘇斯等 |
| 文本批次提取 | ⬜ 未開始 | Implementer | Batch 1~4 待定 |
| 圖譜層 (Kuzu) | ⬜ 未開始 | — | 未來擴展 |
| 視覺化前端 | ⬜ 未開始 | — | 未來擴展 |

---

## 五、常見問答（FAQ for AI）

**Q：Implementer 發現 SCHEMA 有矛盾，怎麼辦？**  
A：不要在對話中爭論。在 `TASKLOG.md` 開一條交接記錄，標記「阻擋問題」，由 Architect 處理。

**Q：Implementer 想新增一個 `layer` 值（如 `sea`），怎麼辦？**  
A：禁止自行新增。先在 `TASKLOG.md` 提案，Architect 審查後統一更新 SCHEMA.md + schema.json。

**Q：Architect 想讓 Implementer 做一批 YAML，怎麼傳達？**  
A：不要依賴對話上下文。在 `TASKLOG.md` 寫清楚：
- 目標檔案路徑
- 參考的原文段落（行號或關鍵字）
- 必須包含的欄位清單
- 任何已知的推斷（inferred）項目

**Q：上下文消失了，怎麼辦？**  
A：根據「上下文恢復流程」重新讀取 `PLAN.md` + `SCHEMA.md` + `TASKLOG.md` + `git log`，即可在 30 秒內恢復。

---

## 六、檔案索引（File Index）

| 檔案 | 用途 | 誰負責更新 |
|------|------|-----------|
| `PLAN.md` | 專案總綱與三階段藍圖 | Architect |
| `SCHEMA.md` | YAML 欄位規範（人類可讀） | Architect |
| `schema.json` | JSON Schema（機器驗證） | Architect |
| `AGENTS.md` | 本文件：AI 協作協議 | Architect |
| `TASKLOG.md` | 交接記錄與任務狀態 | 雙方共同維護 |
| `data/index.yaml` | 大陸與帝國索引 | Architect |
| `data/**/*.yaml` | 具體地點資料 | Implementer |
| `api/main.py` | FastAPI 查詢引擎 | Architect |
| `source/ankora-chronicles.md` | 原始敘事文本（只讀） | 人類 / 不移動 |

---

## 七、版本歷史

| 版本 | 日期 | 變更 |
|------|------|------|
| v0.1 | 2026-05-12 | 初始版本，定義 Architect / Implementer 雙角色與交接協議 |
