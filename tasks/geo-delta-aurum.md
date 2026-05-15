# 子代理任務書：geo-delta-aurum

## 目標
建立 `delta_aurum`（奧魯姆河口三角洲）地理實體 YAML。

## 輸出檔案路徑
`/workspaces/anak-world/data/02-east-caesaric/geographies/delta-aurum.yaml`

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
- `id`: `delta_aurum`
- `name`: 奧魯姆河口三角洲
- `layer`: `geography`
- `region`: 東部（與 aurum_river 一致）
- `empire`: 凱撒里克帝國（與 aurum_river 一致）
- `parent_id`: `ankora`

### 敘事錨定（來自現有 YAML）
- aurum_river.yaml 描述：「每年夏季，河口的泥沙堆積會改變航道，只有熟悉水道的本地引水人才能安全進出」
- aurum_river.yaml 連接：wind_isles（東南方入海口外海）
- wind_isles.yaml 描述：「奧魯姆河出海口外海的珊瑚群島」
- wind_isles.yaml 連接：aurum_river（西北方）
- 命名慣例：凱撒里克帝國使用拉丁語，`Aurum` = 黃金，`Delta` = 三角洲

### 已知的 connections（子代理必須建立）
- `aurum_river`（physical，上游）
- `wind_isles`（physical，東南方外海）
- `east_caesaric`（conceptual，貫穿/核心領土）
- `the_howling_peaks`（conceptual，西方遠處）——可選，若有合理關聯
- `south_libertania`（conceptual，東南方）——若與自由城邦有貿易或領土關聯

### 必須建立的双向連接
當你建立 delta_aurum → wind_isles 的連接後，**必須同時在 wind_isles.yaml 中添加 wind_isles → delta_aurum 的對稱連接**。使用 `StrReplaceFile` 工具修改 wind-isles.yaml。

## 需要推斷（inferred）的項目清單
以下項目 schema 中無直接來源，需要基於地理常識與世界觀推斷，**必須標註 `# inferred: true`**：
- 具體的植被類型（紅樹林？蘆葦？鹽沼草？）
- 氣味細節（鹹淡水混合的獨特氣味）
- 聲音細節（候鳥、潮汐、船帆）
- 是否有常駐聚落或港口
- danger_level 與 access_level

## 禁止事項
- 不得修改 SCHEMA.md 或 schema.json
- 不得修改其他子代理正在寫入的檔案（campus-cinereus.yaml、septempontis-vallis.yaml）
- 不得自行創建新的目錄層級

## 上下文恢復
啟動時請依次讀取：
1. `/workspaces/anak-world/PLAN.md`
2. `/workspaces/anak-world/SCHEMA.md`
3. `/workspaces/anak-world/TASKLOG.md`
4. `/workspaces/anak-world/data/02-east-caesaric/geographies/aurum-river.yaml`
5. `/workspaces/anak-world/data/04-south-libertania/geographies/wind-isles.yaml`
6. `/workspaces/anak-world/source/ankora-chronicles.md`（搜尋 "奧魯姆"、"河口"、"三角洲"、"delta" 等關鍵字）

## 完成標準
- [x] delta-aurum.yaml 已寫入指定路徑
- [x] wind-isles.yaml 已添加 delta_aurum 對稱連接
- [x] 所有必填欄位完整
- [x] atmosphere 四項齊全
- [x] 所有推斷內容標註 `# inferred: true`
- [x] 在本任務書末尾記錄任何問題或假設

---

## 完成記錄

**完成時間**：2026-05-15

### 已建立檔案
- `/workspaces/anak-world/data/02-east-caesaric/geographies/delta-aurum.yaml`

### 已修改檔案
- `/workspaces/anak-world/data/04-south-libertania/geographies/wind-isles.yaml`（添加 `delta_aurum` 對稱連接）

### YAML 語法驗證
- ✅ delta-aurum.yaml 通過 `yaml.safe_load()`
- ✅ wind-isles.yaml 通過 `yaml.safe_load()`

### 問題與假設記錄

1. **命名假設**：採用拉丁文 `Delta Aurum`，與凱撒里克帝國的拉丁語命名慣例（`Aurum River`）保持一致。

2. **金灘港為推斷內容**：`aurum_river.yaml` 僅提及「出海口」與「商船啟航」，未描述具體港口名稱。金灘港（Golden Beach Port）及其燈塔歷史（645年建立）均為基於地理邏輯與帝國擴張敘事的合理推斷，已標註 `# inferred: true`。

3. **人口數據為推斷**：原文與現有 YAML 均未提供三角洲人口。設定三千人是基於「小型貿易港 + 漁村」規模的合理推斷，已標註 `# inferred: true`，且使用 `integer` 型別 `3000` 以符合 `schema.json` 要求。

4. **宗教細節為推斷**：凱撒里克帝國官方信仰為東派正教（見 `east_caesaric/empire.yaml`），漁民私下祭拜水神與風母是基於河口漁民常見信仰的合理推斷，已標註 `# inferred: true`。

5. **植被與生態為推斷**：紅樹林島群、蘆葦叢、鹽沼等具體植被類型未在現有 YAML 或 source text 中明確描述，是基於熱帶/亞熱帶河口三角洲生態的推斷，已標註 `# inferred: true`。

6. **連接選擇**：建立 `south_libertania` 的 conceptual 連接，基於「金灘港是凱撒里克與自由城邦貿易前哨」的敘事定位；未建立 `the_howling_peaks` 連接，因為三角洲與怒嘯山脈之間隔著整個凱撒里克帝國東部，地理關聯過於間接。

7. **危險等級設定為 medium**：雖然三角洲本身並非戰區，但每年夏季泥沙改變航道、水道錯綜複雜，對不熟悉的外來船隻構成實質危險，因此設定為 `medium` 而非 `low`。
