# 任務書：Agent 2 — 格蘭迪斯大公國 + 莫爾根王國（5個Tier3 County）

## 目標
建立以下 5 個 Tier 3 settlement YAML：

### 格蘭迪斯大公國（3個）
1. `data/01-west-seraphion/locations/vinetum-estate.yaml`
   - `id`: `vinetum_estate`
   - `name`: 維內圖姆葡萄園莊園（拉丁 Vinetum = 葡萄園）
   - 定位：格蘭迪斯家族旁支或小貴族的葡萄酒莊園，供應維特魯斯貴族
   - `settlement_type`: `village`
   - `parent_id`: `west_seraphion`
   - `region`: 格蘭迪斯大公國境內

2. `data/01-west-seraphion/locations/molinaria.yaml`
   - `id`: `molinaria`
   - `name`: 莫利納里亞磨坊鎮（拉丁 Molinarius = 磨坊主）
   - 定位：傑米努斯河支流上的水力磨坊村，為周邊農村磨麥
   - `settlement_type`: `village`
   - `parent_id`: `west_seraphion`
   - `region`: 格蘭迪斯大公國境內

3. `data/01-west-seraphion/locations/ruina-damni.yaml`
   - `id`: `ruina_damni`
   - `name`: 魯伊納達姆遺跡村（拉丁 Ruina Damni = 堤壩遺跡）
   - 定位：古代堤壩遺跡周邊的貧民/農民聚落，與現有 `dam_ruins_outpost.yaml` 相鄰
   - `settlement_type`: `village`
   - `parent_id`: `west_seraphion`
   - `region`: 格蘭迪斯大公國境內

### 莫爾根王國（2個）
4. `data/01-west-seraphion/locations/silva-navalis.yaml`
   - `id`: `silva_navalis`
   - `name`: 西爾瓦納瓦利斯伐木谷（拉丁 Silva Navalis = 造船森林）
   - 定位：內陸森林谷地，提供造船木材給潮音宮與私掠艦隊
   - `settlement_type`: `village`
   - `parent_id`: `west_seraphion`
   - `region`: 莫爾根王國境內

5. `data/01-west-seraphion/locations/corallium-cove.yaml`
   - `id`: `corallium_cove`
   - `name`: 科拉利烏姆珊瑚灣（拉丁 Corallium = 珊瑚）
   - 定位：南方海岸小海灣，採集珊瑚與珍珠，與 `pearl_bay_village` 相鄰
   - `settlement_type`: `village`
   - `parent_id`: `west_seraphion`
   - `region`: 莫爾根王國境內

## 規範
- 全部為 Tier 3：單一 YAML，無獨立 district/room
- 參照 `SCHEMA.md` 第二節與第五節
- 必填：`id`, `name`, `layer`, `region`, `empire`, `parent_id`, `description`, `atmosphere`, `tags`
- `atmosphere` 必須包含 `scent`, `light`, `temperature`, `sound`

## 已知連接
- `vinetum_estate` → `golden_spire_castle`（金穗堡，格蘭迪斯大公國首都）
- `molinaria` → `flumen_geminus`（傑米努斯河支流）
- `ruina_damni` → `dam_ruins_outpost`（堤壩遺跡哨站）
- `silva_navalis` → `palace_of_tidal_song`（潮音宮）
- `corallium_cove` → `pearl_bay_village`（珍珠灣漁村）

## 命名風格
- 格蘭迪斯下屬：拉丁文（Vinetum, Molinaria, Ruina Damni）
- 莫爾根下屬：拉丁文（Silva Navalis, Corallium）

## 注意事項
- 全部標註 `inferred: true`（這些是推斷產生的定居點）
- 人口數量需符合 Tier 3 村莊規模（數百至數千人）
- 格蘭迪斯大公國的特徵：糧食壟斷、麥田、中央平原
- 莫爾根王國的特徵：南方海岸、私掠、海洋貿易、珊瑚與珍珠
