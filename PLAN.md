# Ankora-World 計劃：安納克世界地圖引擎

> **執行後，本計劃將同時寫入 `/workspaces/anak-world/PLAN.md`，確保你隨時可在 Codespaces / CLI / GitHub 上查看。**

---

## 背景與目標

將《安納克大陸誌》（2529 行敘事文本）轉化為結構化的靜態 YAML 世界資料庫。核心原則：靜態優先、層次錨定、AI 無關。

## 現狀

- `README.md` + `source/ankora-chronicles.md`（2529 行原始文本）
- 無既有 API、schema、或資料結構代碼

---

## 第一階段：骨架與第一個記憶錨點（本輪執行）

### 1.1 目錄結構

```
ankora-world/
├── PLAN.md                     # ← 本計劃的可見副本
├── README.md
├── SCHEMA.md                   # YAML 欄位規範（人類可讀）
├── schema.json                 # JSON Schema（機器驗證）
├── source/
│   └── ankora-chronicles.md    # 原始文本移入此處
├── data/                       # 權威結構化資料
│   ├── index.yaml              # 五大區域 + 秘境索引
│   ├── 01-west-seraphion/
│   │   ├── empire.yaml
│   │   └── locations/
│   │       └── vetustapolis/
│   │           └── inner-city/
│   │               └── sacred-key-complex.yaml
│   ├── 02-east-caesaric/
│   ├── 03-north-frost/
│   ├── 04-south-libertania/
│   └── 05-secret-eldara/
├── api/                        # FastAPI 查詢引擎
│   ├── main.py
│   └── requirements.txt
└── site/                       # 靜態前端（預留）
    └── .gitkeep
```

### 1.2 技術骨架（FastAPI + Pydantic + YAML）

- **啟動載入**：遞迴掃描 `data/` 下所有 `.yaml`，以 `id` 為 key 載入記憶體 dict
- **資料驗證**：Pydantic 模型於啟動時驗證所有 YAML，遇錯即拋出明確錯誤
- **四個端點**：
  - `GET /location/{id}` — 單一地點完整 JSON
  - `GET /location/{id}/neighbors` — connections 展開
  - `GET /search?q=` — 跨地點關鍵字搜尋
  - `GET /hierarchy?region=` — 層次樹
- **健康檢查**：`GET /health` 回傳載入統計

### 1.3 第一個示範地點：聖鑰院複合體

從原始文本提取核心資訊，建立 `sacred-key-complex.yaml`，作為所有後續 YAML 的黃金範本。

### 1.4 SCHEMA.md 與 schema.json

定義五級層次（continent → empire → city → district → room）與必填欄位，讓未來協作者（人類或 AI）知道如何新增地點。

---

## 第二階段：從 2529 行文本提取「每個細節」的方法論

> **核心問題：如何把線性敘事，轉化為結構化的空間座標系？**

### 2.1 文本掃描策略（建議用 AI 輔助批次處理）

1. **地理實體識別**
   - 遍歷全文，標記所有地名、建築名、區域名
   - 分類層級：帝國（Empire）→ 城市（City）→ 區域（District）→ 房間（Room）
   - 範例：塞拉菲昂神聖帝國 → 維斯塔波利斯 → 內城區 → 聖鑰院複合體

2. **關係圖譜抽取**
   - 從敘事中識別「A 位於 B 之內」、「C 通往 D」、「E 隸屬於 F」
   - 轉化為 YAML 的 `connections` 與 `parent_id` 機制

3. **感官錨定抽取**
   - 掃描文本中的感官描述詞：氣味（薰香、腐臭、松脂）、光線（燭火、夕照、漆黑）、聲音（禱告、風聲、金屬撞擊）
   - 若原文未明確描述，根據場景性質進行合理推斷並標記 `inferred: true`

4. **歷史事件綁定**
   - 識別文本中的年份、事件名稱，綁定到相關地點的 `events[]`

### 2.2 分批實施建議

不建議一次性處理全書 2529 行（易出錯且難以驗證）。建議按卷分批：

| 批次 | 內容 | 預估地點數 | 策略 |
|------|------|-----------|------|
| Batch 1 | 第六卷「世界地圖」+ 第十~十二卷帝國詳考 | ~30-50 | 原文最密集的地理描述，優先結構化 |
| Batch 2 | 第一~五卷編年史中的關鍵場景 | ~20-30 | 提取歷史事件發生地 |
| Batch 3 | 第七~九卷魔法、社會、英雄傳說 | ~15-25 | 補充秘境、地下設施等特殊地點 |
| Batch 4 | 序章與附錄 | ~5-10 | 世界樹、星隕深淵等宏觀地點 |

### 2.3 品質控制機制

- **黃金範本對齊**：所有新 YAML 必須與 `sacred-key-complex.yaml` 的欄位一致
- **JSON Schema 驗證**：提交前自動跑 `schema.json` 驗證
- **交叉引用檢查**：確保 `connections[].target` 指向的 `id` 真實存在
- **Git Diff 審查**：每次批次處理後人類快速瀏覽 diff，確認無幻覺或錯誤推斷

### 2.4 感官細節的填充原則

- **原文有則錄**：文本明確寫到的感官描述直接收錄
- **原文無則推**：根據場景性質合理推斷（如地牢 → 潮濕霉味、微弱燭光），但必須標記 `inferred: true`
- **不確定則空**：若無法合理推斷，留空 `null` 或 `[]`，不強求填滿

---

## 第三階段：未來擴展（本輪不執行，僅預留）

- **圖譜層**：引入 Kuzu 嵌入式圖資料庫，支援複雜圖查詢（最短路徑、勢力範圍）
- **視覺化**：React + Cytoscape.js 靜態網頁，GitHub Pages 托管
- **AI 敘事層**：MCP / Function Calling 接口，讓 Claude / Gemini 透過 API 讀取世界資料
- **多 Agent 管線**：參考 ai-dungeon-master 的 LangGraph 設計，啟動劇場模式

---

## 執行順序與預估時間

| 步驟 | 內容 | 時間 |
|------|------|------|
| 1 | 建立目錄結構 + PLAN.md | 5 min |
| 2 | 撰寫 SCHEMA.md + schema.json | 10 min |
| 3 | 撰寫 api/main.py（FastAPI 骨架 + 四端點） | 20 min |
| 4 | 建立示範地點 sacred-key-complex.yaml | 10 min |
| 5 | 安裝依賴 + 啟動 uvicorn + curl 測試 | 5 min |
| 6 | git commit | 2 min |
| **總計** | | **~52 min** |

---

## 一句話指令（執行確認後）

> 請開始執行第一階段：建立目錄結構、撰寫 SCHEMA.md 與 schema.json、建立 FastAPI 骨架與四個核心端點、建立聖鑰院示範 YAML，並透過 uvicorn 本地驗證後提交 Git。
