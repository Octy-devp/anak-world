# 子代理任務書：geo-campus-cinereus

## 目標
建立 `campus_cinereus`（東部灰燼荒地）地理實體 YAML。

## 輸出檔案路徑
`/workspaces/anak-world/data/02-east-caesaric/geographies/campus-cinereus.yaml`

> **注意**：目標目錄已存在（`data/02-east-caesaric/geographies/`），直接寫入即可。

## SCHEMA 規範（摘要）
- 參考 `/workspaces/anak-world/SCHEMA.md` 的 `geography` 層級規範
- 必填欄位：`id`, `name`, `layer`, `region`, `empire`, `parent_id`, `description`, `atmosphere`, `tags`
- `layer` 必須為 `geography`
- `id` 使用 snake_case
- `atmosphere` 必須包含：`scent[]`, `light`, `temperature`, `sound[]`
- 推斷內容必須標註 `# inferred: true`
- 權威性優先級：`data/*/geographies/*.yaml` > `data/*/empire.yaml` > `source/ankora-chronicles.md`

## 已知錨定資訊

### 身份錨定
- `id`: `campus_cinereus`
- `name`: 東部灰燼荒地（或灰燼平原）
- `layer`: `geography`
- `region`: 東部
- `empire`: 凱撒里克帝國
- `parent_id`: `ankora`

### 敘事錨定（來自現有 YAML 與推斷）
- 命名慣例：`Campus` = 平原/場地，`Cinereus` = 灰色/灰燼色。凱撒里克帝國使用拉丁語命名。
- 位置推斷：東部內陸，aurum_river 上游山區以東，the_howling_peaks 東麓延伸地帶。
- 特徵推斷：大洪水時期隕鐵撞擊或火山活動後的荒涼地帶，地表覆蓋灰色火山灰或風化隕鐵碎屑，植被稀疏。
- 與 howling_peaks 的關聯：howling_peaks 描述「大洪水時期地殼撕裂形成的褶皺山脈」，東坡「背風乾燥，岩石裸露，風蝕嚴重」。灰燼荒地可能是這種地質的東部延伸。
- 與 aurum_river 的關聯：aurum_river 發源於「東部山區」，灰燼荒地可能位於上游流域東側。

### 已知的 connections（子代理必須建立）
- `east_caesaric`（conceptual，貫穿/核心領土）
- `the_howling_peaks`（physical，西方）——地質延伸關係
- `aurum_river`（physical，北方/西北方）——上游流域關係
- `septempontis_vallis`（physical，東方/東北方）——與七橋峽谷相鄰

### 必須建立的双向連接
當你建立 campus_cinereus → the_howling_peaks 的連接後，**必須同時在 the-howling-peaks.yaml 中添加 the_howling_peaks → campus_cinereus 的對稱連接**。使用 `StrReplaceFile` 工具修改 the-howling-peaks.yaml。

## 需要推斷（inferred）的項目清單
以下項目 schema 中無直接來源，需要基於地理常識與世界觀推斷，**必須標註 `# inferred: true`**：
- 灰燼的具體來源（火山？隕鐵撞擊？大洪水後的沉積？）
- 是否有礦產或資源（隕鐵碎屑？稀有礦物？）
- 是否有游牧民族或邊境哨站
- 氣味細節（火山灰、硫磺、乾燥塵土）
- 聲音細節（風嘯、遠處山崩）
- danger_level 與 access_level

## 禁止事項
- 不得修改 SCHEMA.md 或 schema.json
- 不得修改其他子代理正在寫入的檔案（delta-aurum.yaml、septempontis-vallis.yaml）
- 不得自行創建新的目錄層級

## 上下文恢復
啟動時請依次讀取：
1. `/workspaces/anak-world/PLAN.md`
2. `/workspaces/anak-world/SCHEMA.md`
3. `/workspaces/anak-world/TASKLOG.md`
4. `/workspaces/anak-world/data/01-west-seraphion/geographies/the-howling-peaks.yaml`
5. `/workspaces/anak-world/data/02-east-caesaric/geographies/aurum-river.yaml`
6. `/workspaces/anak-world/source/ankora-chronicles.md`（搜尋 "灰燼"、"荒地"、"東部"、"campus"、"cinereus" 等關鍵字）

## 完成標準
- [x] campus-cinereus.yaml 已寫入指定路徑
- [x] the-howling-peaks.yaml 已添加 campus_cinereus 對稱連接
- [x] 所有必填欄位完整
- [x] atmosphere 四項齊全
- [x] 所有推斷內容標註 `# inferred: true`
- [x] 在本任務書末尾記錄任何問題或假設

---

## 問題與假設記錄（子代理完成後填寫）

### 1. 地理位置假設
- 灰燼荒地的具體位置無法從 source text 直接確認。任務書給出的推斷位置（aurum_river 上游山區以東、the_howling_peaks 東麓延伸）是唯一可用的空間錨定。本 YAML 據此建立，但實際邊界為推斷。

### 2. 「灰燼的焚燒」（第395年）的地理歸屬問題
- source text 記載第395年「燼地農人」發動「灰燼的焚燒」，最終在傑米努斯河畔被鎮壓。由於傑米努斯河位於大陸中央（魯普圖斯隘口），而 campus_cinereus 被推斷於東部內陸，兩者的地理位置可能並不一致。
- **決定**：未將「灰燼的焚燒」事件直接寫入 campus-cinereus.yaml，避免地理錯誤。改以推斷的「灰燼商道開闢」（第780年）作為歷史事件，來源為「面對利貝塔尼亞海峽封鎖」的敘事背景（source text 第1758行）。

### 3. septempontis_vallis 與 delta_aurum 的交叉引用
- 任務書要求建立對 septempontis_vallis 的連接，但 data/ 目錄中該 YAML 尚未存在（其他子代理負責）。connections 中已保留此連接，待後續子代理建立該檔案後即可解析閉合。

### 4. 火山活動與隕鐵撞擊的雙重成因
- source text 明確提及「灰燼商道穿越東方邊境的廢棄火山帶」，但未說明火山與隕鐵的確切關係。description 中將兩者並列為「大洪水時期的地殼撕裂與隕鐵撞擊」的綜合結果，此為推斷，已於多處標註 `# inferred: true`。

### 5. 感官細節
- 所有 atmosphere 欄位除「灰燼商道駝隊的鈴鐺與車輪聲」有 source text 直接支撐外，其餘均為基於「廢棄火山帶」與「荒涼平原」性質的合理推斷，已逐一標註。

### 6. 本次執行確認（2026-05-15）
- `campus-cinereus.yaml` 已成功建立於 `data/02-east-caesaric/geographies/`。
- `the-howling-peaks.yaml` 已添加對 `campus_cinereus` 的對稱連接（東麓延伸）。
- `septempontis-vallis.yaml` 已由其他子代理完成並包含對 `campus_cinereus` 的連接（西南方），雙向引用現已閉合。
- 所有必填欄位完整，atmosphere 四項齊全，推斷內容已標註 `# inferred: true`。
- 未修改 `delta-aurum.yaml` 或其他子代理負責的檔案。
