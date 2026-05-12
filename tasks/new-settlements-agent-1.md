# 任務書：Agent 1 — 特殊地點：劍誓池

## 目標
建立 `data/01-west-seraphion/locations/sword-oath-pool.yaml`

## 背景
劍誓池（Pool of Sword-Oath）是東西兩大帝國正統性敘事的共同歷史錨點。
Source 同時提到「維特魯斯郊外的劍誓池」和「奧斯堡的劍誓池」，
最合理的解釋是：原始劍誓池在維特魯斯郊外（歷史遺跡），東遷後凱撒里克在奧斯堡複製/重建了一個。
本檔案建立的是**塞拉菲昂境內的原版劍誓池**（維特魯斯郊外）。

## Source 參考
- ankora-chronicles.md 第 352 行：馬庫斯救出幼帝後在維特魯斯郊外劍誓池旁駐紮三天，公開祭拜艾森瓦爾五世骨灰。
- ankora-chronicles.md 第 1700 行：帝國軍團騎士受封時以隕鐵劍割掌，滴血入劍誓池，宣誓「劍不折，膝不屈，背不向敵」。
- ankora-chronicles.md 第 1800 行：瓦萊里安將密信灰燼撒入劍誓池——凱撒里克對西部偽朝最輕蔑的回應。

## 規範
- 參照 `SCHEMA.md` 第五節：Tier 3 單一 YAML（普通 County）
- 參照 `SCHEMA.md` 第二節：單一地點 YAML 結構
- `id`: `sword_oath_pool`（snake_case）
- `layer`: `settlement`
- `region`: 夕照畿郊外
- `empire`: 塞拉菲昂神聖帝國
- `parent_id`: `west_seraphion`
- `settlement_type`: `monastery` 或 `outpost`（根據描述判斷，這是一個具有宗教/軍事儀式功能的遺跡地點）

## 已知連接
- `connections` 應指向 `vetustapolis`（維特魯斯郊外）
- 可選：與 `the_flood_plain`（中央沖積平原）的 conceptual 連接

## 命名風格
- 拉丁文風格。`Pool of Sword-Oath` = Puteus Gladii Juramenti（劍誓之井）
- 人類可讀名稱用中文音譯或意譯。

## 注意事項
- 必須標註 `inferred: true` 於所有非 source 直接描述的細節
- 不要與 `data/02-east-caesaric/` 下的奧斯堡產生直接矛盾（東西帝國各自宣稱正統性是可以接受的敘事張力）
