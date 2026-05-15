# 子代理任務書：geo-septempontis-vallis-fix（修正版）

## 目標
**重寫** `septempontis-vallis.yaml`，修正所有違反故事設定的內容。

## 輸出檔案路徑
`/workspaces/anak-world/data/02-east-caesaric/geographies/septempontis-vallis.yaml`

## 必須遵守的設定事實（來自 source/ankora-chronicles.md）

### 東方大遷徙路線（第726-729年）
- 起點：維特魯斯（西部）
- 路線：**穿越阿比蘇斯裂谷**（南部大斷裂帶）→ 向東方平原進發
- 終點：傑米努斯河東岸的特爾馬嶺，建立奧斯堡
- **東遷隊伍不經過奧魯姆河上游，不經過七橋峽谷**
- 東遷遭遇的霜生襲擾：發生在阿比蘇斯裂谷/博雷阿利斯附近（北方遊牧民族季節性南下），**不是在凱撒里克東部內陸**

### 霜生（The Frostborn）
- 北方獨立文明，不屬於北境諸邦
- 主要活動範圍在極北/北境
- **不會出現在凱撒里克東部內陸的奧魯姆河上游**

### 馬庫斯·克羅諾斯
- 東遷領袖，但東遷路線與奧魯姆河上游無關
- **不得虛構「馬庫斯穿越七橋峽谷」的事件**

## 修正要求

### 必須刪除的內容
- [ ] 任何將「東方大遷徙」與七橋峽谷關聯的描述
- [ ] 任何「霜生部隊/霜生偵察小隊出現在七橋峽谷」的描述
- [ ] 任何「馬庫斯親王在七橋峽谷建橋/過橋」的事件
- [ ] tag 中的 `東方大遷徙`

### 新的敘事框架（基於地理與政治邏輯）
七橋峽谷是奧魯姆河上游的天然峽谷，河流切穿東部山脈形成。七座橋是凱撒里克帝國為了連接東部山區與平原、控制東西/南北交通而**在不同歷史時期陸續修建**的。可以設定：
- 最底層的橋：古代遺跡或早期邊疆領主所建的簡易木橋/吊橋（與東遷無關）
- 中層橋：帝國初年或攝政時期修建的石拱橋，供軍隊與商旅
- 最高層的「攝政橋」：近年新建的鐵索橋，可容四馬並行，橋頭有克羅諾斯家族紋章
- 「斷橋」：因**山崩或洪水**坍塌，可保留傳說但**不得涉及霜生或東遷**

### 必須保留的連接
- `aurum_river`（physical，貫穿）
- `east_caesaric`（conceptual，核心領土）
- `the_howling_peaks`（physical，西方）
- `campus_cinereus`（physical，西南方）

### 對稱連接
- `aurum-river.yaml` 已有 `septempontis_vallis` 連接，無需修改

## SCHEMA 規範
- 參考 `/workspaces/anak-world/SCHEMA.md` 的 `geography` 層級
- 必填欄位完整，atmosphere 四項齊全
- 推斷內容標註 `# inferred: true`

## 禁止事項
- 不得將東遷與此地關聯
- 不得將霜生設定在此地
- 不得修改 SCHEMA.md 或 schema.json
- 不得修改其他 YAML

## 上下文恢復
1. `/workspaces/anak-world/SCHEMA.md`
2. `/workspaces/anak-world/data/02-east-caesaric/geographies/aurum-river.yaml`
3. `/workspaces/anak-world/data/01-west-seraphion/geographies/the-howling-peaks.yaml`
4. `/workspaces/anak-world/data/02-east-caesaric/geographies/campus-cinereus.yaml`
5. `/workspaces/anak-world/data/02-east-caesaric/empire.yaml`
6. `/workspaces/anak-world/source/ankora-chronicles.md`（搜尋「東方大遷徙」「東遷」「馬庫斯」「霜生」確認路線）

## 完成標準
- [ ] 完全刪除東遷與霜生相關內容
- [ ] 建立符合設定的七橋歷史
- [ ] atmosphere 四項齊全
- [ ] 所有推斷標註 `# inferred: true`
- [ ] YAML 語法正確
