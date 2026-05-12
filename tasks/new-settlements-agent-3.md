# 任務書：Agent 3 — 西爾伯弗羅斯特邊疆大公國 + 瓦羅蘭特直轄（4個Tier3 County）

## 目標
建立以下 4 個 Tier 3 settlement YAML：

### 西爾伯弗羅斯特邊疆大公國（3個）
1. `data/01-west-seraphion/locations/isgrav.yaml`
   - `id`: `isgrav`
   - `name`: 伊斯格拉夫冰墓（諾德 Is + grav = 冰墓）
   - 定位：被白霜寒法瞬間冰封的廢棄村落，構成無聲邊界標記。Source 多次強調「邊境線上無數冰墓靜靜矗立」。
   - `settlement_type`: `village`（廢棄村落）
   - `parent_id`: `west_seraphion`
   - `region`: 西爾伯弗羅斯特邊境

2. `data/01-west-seraphion/locations/frostborg.yaml`
   - `id`: `frostborg`
   - `name`: 弗羅斯特堡（諾德 Frost + borg = 霜堡）
   - 定位：《霜戒法》後改造的地下冰窖軍事堡壘，村民轉為軍事編制
   - `settlement_type`: `fortress`
   - `parent_id`: `west_seraphion`
   - `region`: 西爾伯弗羅斯特邊境

3. `data/01-west-seraphion/locations/vaktorn.yaml`
   - `id`: `vaktorn`
   - `name`: 瓦克托恩哨站（諾德 Vakt + torn = 守望塔）
   - 定位：監控白霜動向的最前線哨站，駐紮寒法師獵人
   - `settlement_type`: `outpost`
   - `parent_id`: `west_seraphion`
   - `region`: 西爾伯弗羅斯特邊境

### 瓦羅蘭特皇室直轄（1個）
4. `data/01-west-seraphion/locations/venatorium.yaml`
   - `id`: `venatorium`
   - `name`: 維納托里烏姆狩獵莊園（拉丁 Venatorium = 狩獵場）
   - 定位：瓦羅蘭特皇室的私人狩獵莊園，位於維特魯斯近郊森林中，象徵皇室僅存的特權之一
   - `settlement_type`: `village` 或 `fortress`
   - `parent_id`: `west_seraphion`
   - `region`: 夕照畿

## 規範
- 全部為 Tier 3：單一 YAML，無獨立 district/room
- 參照 `SCHEMA.md` 第二節與第五節
- 必填：`id`, `name`, `layer`, `region`, `empire`, `parent_id`, `description`, `atmosphere`, `tags`
- `atmosphere` 必須包含 `scent`, `light`, `temperature`, `sound`

## 已知連接
- `isgrav` → `frostspire`（霜尖塔要塞，西爾伯弗羅斯特首都）
- `frostborg` → `frostspire`
- `vaktorn` → `frostspire` 與 `northern_mountains`（約恩維德山脈，北境方向）
- `venatorium` → `vetustapolis`（維特魯斯近郊）

## 命名風格
- 西爾伯弗羅斯特下屬：諾德文/斯拉夫風格（Isgrav, Frostborg, Vaktorn）
- 瓦羅蘭特直轄：拉丁文（Venatorium）

## Source 參考
- 冰墓：ankora-chronicles.md 第 543, 602, 670, 1493 行
- 霜戒法與邊境堡壘：ankora-chronicles.md 第 1493 行

## 注意事項
- 全部標註 `inferred: true`
- 西爾伯弗羅斯特特徵：極端軍事化神權、冰防役、白霜威脅、寒法師
- 瓦羅蘭特直轄特徵：皇室衰微、僅存特權、小冰期影響
