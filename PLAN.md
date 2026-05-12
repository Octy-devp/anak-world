# Ankora-World 計劃：安納克世界地圖引擎

> **執行後，本計劃將同時寫入 `/workspaces/anak-world/PLAN.md`，確保你隨時可在 Codespaces / CLI / GitHub 上查看。**

---

## 背景與目標

將《安納克大陸誌》（2529 行敘事文本）轉化為結構化的靜態 YAML 世界資料庫。核心原則：靜態優先、層次錨定、AI 無關。

## 現狀

- `README.md` + `source/ankora-chronicles.md`（2529 行原始文本）
- Schema v0.3 + `schema.json`（機器驗證通過）
- AGENTS.md v0.3（子代理協作協議 + 數據來源優先級）
- **31 個 YAML 檔案**已完成：`index.yaml` + 14 geography + 5 empire + 11 settlement
- Git `main` 分支領先 origin 約 15 個提交

---

## 第一階段：骨架與第一個記憶錨點 ✅ 已完成

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

定義五級層次（continent → empire → settlement → district → room）與必填欄位，讓未來協作者（人類或 AI）知道如何新增地點。

---

## 第二階段：從 2529 行文本提取「每個細節」 ✅ 已完成

> **核心問題：如何把線性敘事，轉化為結構化的空間座標系？**
> 
> **答案**：三層並行批次處理 + 父代理驗證 + geography 權威優先。

### 2.1 已完成的批次處理

| 批次 | 內容 | 實際產出 | 狀態 |
|------|------|---------|------|
| Batch 1 | Geography 層（山脈、河流、深淵、群島、世界樹） | 14 YAMLs | ✅ |
| Batch 2 | Empire 層（五大帝國） | 5 YAMLs | ✅ |
| Batch 3 | Settlement 層（首都 + 要塞 + 村莊 + 修道院） | 11 YAMLs | ✅ |
| Batch 4 | 一致性修正與歷史補充 | 塔拉薩七海同盟、連接方式修正等 | ✅ |

### 2.2 數據來源優先級（AGENTS.md v0.3）

建立任何地點時必須遵循：
1. **`geography` YAML** > `empire` YAML > `source/ankora-chronicles.md` > 推斷
2. 推斷內容必須標註 `# inferred: true`
3. 若 source 與已結構化的 geography 衝突，**以 geography 為準**

1. **地理實體識別**
   - 遍歷全文，標記所有地名、建築名、區域名
   - 分類層級：帝國（Empire）→ 定居點（Settlement）→ 區域（District）→ 房間（Room）
   - 範例：塞拉菲昂神聖帝國 → 維斯塔波利斯 → 內城區 → 聖鑰院複合體

2. **關係圖譜抽取**
   - 從敘事中識別「A 位於 B 之內」、「C 通往 D」、「E 隸屬於 F」
   - 轉化為 YAML 的 `connections` 與 `parent_id` 機制

3. **感官錨定抽取**
   - 掃描文本中的感官描述詞：氣味（薰香、腐臭、松脂）、光線（燭火、夕照、漆黑）、聲音（禱告、風聲、金屬撞擊）
   - 若原文未明確描述，根據場景性質進行合理推斷並標記 `inferred: true`

4. **歷史事件綁定**
   - 識別文本中的年份、事件名稱，綁定到相關地點的 `events[]`

### 2.3 品質控制機制（已落實）

- ✅ **JSON Schema 驗證**：每次提交前自動驗證 `schema.json`
- ✅ **交叉引用檢查**：`connections[].target` 必須指向真實存在的 `id`
- ✅ **Geography 一致性檢查**：子代理並行驗證 settlement 與 geography 的空間/氣候/連接一致性
- ✅ **Git Diff 審查**：每批次處理後人類審查 diff
- ✅ **數據來源標註**：推斷內容強制標記 `# inferred: true`

### 2.4 感官細節的填充原則

- **原文有則錄**：文本明確寫到的感官描述直接收錄
- **原文無則推**：根據場景性質合理推斷，但必須標記 `inferred: true`
- **不確定則空**：若無法合理推斷，留空 `null` 或 `[]`，不強求填滿

---

## 第三階段：下一輪待執行

### 3.1 District / Room 層級
- 維特魯斯三層空間：inner_city（聖鑰院、暮光宮）、lower_city（百工坊、橋樑市集）、beyond_walls（灰土園、靜默之塔）
- 奧斯堡同心圓：冰壁宮、霜誓廳、破曉號角
- 其他 settlement 的內部區域

### 3.2 勢力層（Faction Layer）
- 霜刃傭兵團（Frostblade Company）
- 銀葉商會（Silverleaf Guild）
- 黑曜石守望者（Obsidian Watch）
- 赭石行會（Ochre Guild）
- 普世教會東西兩派
- 通用欄位：`type`, `headquarters`, `founding_year`, `ideology`, `influence[]`, `relations[]`, `members[]`

### 3.3 FastAPI 查詢引擎
- `GET /location/{id}` — 單一地點完整 JSON
- `GET /location/{id}/neighbors` — connections 展開
- `GET /search?q=` — 跨地點關鍵字搜尋
- `GET /hierarchy?region=` — 層次樹
- `GET /settlement/{id}`（v0.3 路由）

### 3.4 未來擴展（預留）
- **圖譜層**：Kuzu 嵌入式圖資料庫
- **視覺化**：React + Cytoscape.js 靜態網頁
- **AI 敘事層**：MCP / Function Calling 接口

---

## 執行順序與預估時間（已執行 + 待執行）

| 階段 | 內容 | 狀態 | 實際時間 |
|------|------|------|---------|
| 1 | 建立目錄結構 + PLAN.md + AGENTS.md | ✅ | ~30 min |
| 2 | 撰寫 SCHEMA.md v0.1 + schema.json | ✅ | ~20 min |
| 3 | Geography 層 14 YAMLs（兩批次） | ✅ | ~2 hrs |
| 4 | Empire 層 5 YAMLs + 驗證 | ✅ | ~1.5 hrs |
| 5 | Schema v0.3（city → settlement + CKII 類型） | ✅ | ~30 min |
| 6 | Settlement 層 11 YAMLs（兩批次 + 修正） | ✅ | ~2.5 hrs |
| 7 | 塔拉薩歷史補充 + 連接方式修正 | ✅ | ~20 min |
| **下一輪** | | | |
| 8 | District / Room 層級 | ⏳ | 待定 |
| 9 | Faction 層 4-6 YAMLs | ⏳ | 待定 |
| 10 | FastAPI 骨架 + 四端點 | ⏳ | 待定 |

---

## 一句話指令（下一輪）

> 請選擇執行第三階段任務：建立 District/Room 層級 YAML、建立 Faction 層級 YAML、或建立 FastAPI 查詢引擎。
