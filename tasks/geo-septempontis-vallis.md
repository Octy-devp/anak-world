# 子代理任務書：geo-septempontis-vallis

## 目標
建立 `septempontis_vallis`（七橋峽谷）地理實體 YAML。

## 輸出檔案路徑
`/workspaces/anak-world/data/02-east-caesaric/geographies/septempontis-vallis.yaml`

> **注意**：目標目錄已存在（`data/02-east-caesaric/geographies/`），直接寫入即可。

## SCHEMA 規範（摘要）
- 參考 `/workspaces/anak-world/SCHEMA.md` 的 `geography` 層級規範
- 必填欄位：`id`, `name`, `layer`, `region`, `empire`, `parent_id`, `description`, `atmosphere`, `tags`
- `layer` 必須為 `geography`
- `id` 使用 snake_case
- `atmosphere` 必須包含：`scent[]`, `light`, `temperature`, `sound[]`
- 推斷內容必須標註 `# inferred: true`
- 權威性優先級：`data/*/geographies/*.yaml` > `data/*/empire.yaml` > `source/ankora-chronicles.md`

## 核心設定事實（來自 source/ankora-chronicles.md，不可違反）

### 東方大遷徙路線（第726-729年）
- **起點**：維特魯斯（西部）
- **路線**：穿越**阿比蘇斯裂谷**（南部大斷裂帶）→ 向東方平原進發
- **終點**：傑米努斯河東岸的特爾馬嶺，建立奧斯堡
- **關鍵事實**：東遷隊伍**不經過奧魯姆河上游**，**不經過七橋峽谷**
- 東遷遭遇的追殺者：
  1. **巴爾塔薩的赤土農民軍**（塞拉菲昂方面）——第727年春在「裂谷隘口」追上東遷隊伍，發生「裂谷血戰」
  2. **霜生殘部**（博雷阿利斯白色遊牧民）——在遷徙途中夜間偷襲營地邊緣，擄走牲畜與婦女
- 東遷與奧魯姆河上游/七橋峽谷**無地理關聯**

### 霜生（The Frostborn）
- 北方獨立文明，主要活動範圍在極北/北境
- 不會出現在凱撒里克東部內陸的奧魯姆河上游

## 身份錨定
- `id`: `septempontis_vallis`
- `name`: 七橋峽谷
- `layer`: `geography`
- `region`: 東部
- `empire`: 凱撒里克帝國
- `parent_id`: `ankora`

## 敘事框架（基於地理與政治邏輯）
七橋峽谷是奧魯姆河上游的天然峽谷，河流切穿東部山脈形成。七座橋是凱撒里克帝國為了連接東部山區與平原、控制東西/南北交通而**在不同歷史時期陸續修建**的。
- **最底層橋**：前帝國時代邊疆領主所建的簡易吊橋/古橋遺跡（與東遷無關）
- **中層橋**：帝國初年修建的石拱橋，供軍隊與商旅
- **最高層「攝政橋」**：近年新建的鐵索橋，橋頭有克羅諾斯家族紋章
- **「斷橋」**：因山崩或洪水坍塌，可保留傳說但**不得涉及霜生或東遷**

## 已知的 connections（必須建立）
- `aurum_river`（physical，貫穿）——河流切穿峽谷
- `east_caesaric`（conceptual，核心領土）
- `the_howling_peaks`（physical，西方）——山脈鄰接
- `campus_cinereus`（physical，西南方）——與灰燼荒地相鄰

## 必須建立的双向連接
建立本檔案後，**必須**在 `aurum-river.yaml` 中添加 `aurum_river → septempontis_vallis` 的對稱連接。使用 `StrReplaceFile` 工具修改。

## 禁止事項
- **絕對禁止**將「東方大遷徙」與七橋峽谷關聯
- **絕對禁止**將霜生設定在七橋峽谷
- 不得虛構「馬庫斯親王在七橋峽谷建橋/過橋/被追殺」的事件
- 不得修改 SCHEMA.md 或 schema.json

## 上下文恢復
啟動時請依次讀取：
1. `/workspaces/anak-world/PLAN.md`
2. `/workspaces/anak-world/SCHEMA.md`
3. `/workspaces/anak-world/TASKLOG.md`
4. `/workspaces/anak-world/data/02-east-caesaric/geographies/aurum-river.yaml`
5. `/workspaces/anak-world/data/01-west-seraphion/geographies/the-howling-peaks.yaml`
6. `/workspaces/anak-world/data/02-east-caesaric/empire.yaml`
7. `/workspaces/anak-world/source/ankora-chronicles.md`（搜尋「東方大遷徙」「東遷」「馬庫斯」「霜生」「阿比蘇斯」「裂谷」確認路線）

## 完成標準
- [ ] septempontis-vallis.yaml 已寫入指定路徑
- [ ] aurum-river.yaml 已添加 septempontis_vallis 對稱連接
- [ ] 所有必填欄位完整，atmosphere 四項齊全
- [ ] 所有推斷內容標註 `# inferred: true`
- [ ] **無東遷/霜生違規內容**
- [x] 在本任務書末尾記錄任何問題或假設

## 問題與假設記錄（子代理 geo-septempontis-vallis）

### 1. `campus_cinereus` 檔案尚未存在
- `septempontis-vallis.yaml` 中已建立指向 `campus_cinereus` 的 connection，但 `data/02-east-caesaric/geographies/campus-cinereus.yaml` 目前不存在於檔案系統中。
- **假設**：另一個子代理（geo-campus-cinereus）將負責建立該檔案，屆時雙向連接將自然閉合。

### 2. 七橋峽谷的原始敘事支撐極少
- `source/ankora-chronicles.md` 中完全未提及「七橋峽谷」「Septempontis Vallis」或「奧魯姆河上游峽谷」。
- 所有七座橋的名稱、歷史、結構與社會功能均為推斷，已於 YAML 中標註 `# inferred: true`。

### 3. 修正前版本的 `# inferred: true` 格式問題
- 接收任務時，`septempontis-vallis.yaml` 已存在（但未提交 git），其 `description`、`light`、`temperature` 與多個 `contents/events[].description` 欄位使用了 `>` block scalar，並將 `# inferred: true` 寫在 block scalar 內部。
- 在 YAML 語法中，block scalar 內部的 `#` 不會被解析為註解，而是成為字串值的一部分。子代理已將所有這類註解移動至 key 的同一行（如 `description: >  # inferred: true`），確保機器驗證時不會將註解文字混入實際內容。

### 4. 東遷/霜生合規確認
- 已逐行審查 `septempontis-vallis.yaml`，確認無「東方大遷徙」「東遷」「霜生」相關描述。
- 「霜誓橋」之名來自凱撒里克帝國的「霜誓廳」（Ostburg 主殿），與北方霜生部族無關。
- 「冬季結霜」為純粹氣候描述，無關霜生文明。
