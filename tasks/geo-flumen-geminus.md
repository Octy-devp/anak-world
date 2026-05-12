# 子代理任務書：傑米努斯大河（Flumen Geminus）

## 目標
建立 `data/01-west-seraphion/geographies/flumen-geminus.yaml`（層級：`geography`）

## 核心定位
安納克大陸的**母親河**、**東西動脈**、**文明搖籃**。東西貫穿整片大陸，是所有帝國與城邦的生命線。

## 已知事實（不可違背）
- 東西貫穿大陸的主河流
- 發源於西部高地（可能靠近世界樹區域）
- 貫穿怒嘯山脈的魯普圖斯隘口
- 約恩維德河在北段從北方匯入
- 希爾薇恩河在西段從南方（世界樹方向）匯入
- 中游形成中央沖積平原（三河交匯）
- 最終注入東部或東南部海洋
- 風息群島位於東南海域
- 奧魯姆河是凱撒里克境內獨立的東南向河流

## 與其他 Geography 的連接（必須寫入 connections）

```yaml
connections:
  - target: the_howling_peaks
    type: physical
    direction: 中央段貫穿
    description: 河流從魯普圖斯隘口切穿怒嘯山脈，是東西唯一的便捷水路
  - target: ruptus_pass
    type: physical
    direction: 中央段
    description: 隘口是河流切穿山脈之處，水流湍急，兩岸峭壁如刀削
  - target: northern_mountains
    type: physical
    direction: 北段
    description: 約恩維德河從北部山脈發源，在此匯入主河
  - target: jarnvid_river
    type: physical
    direction: 北岸匯入
    description: 約恩維德河攜帶冰川融水與礦物質，在此匯入，使北岸水質冷冽清澈
  - target: eldara_worldtree
    type: physical
    direction: 西段南岸
    description: 希爾薇恩河從世界樹森林流出，帶著樹脂與落葉的淡金色，在此匯入
  - target: sylvaine_river
    type: physical
    direction: 西段南岸匯入
    description: 希爾薇恩河的匯流點，兩水交會處可見淡金與泥黃的分界線
  - target: the_flood_plain
    type: physical
    direction: 中游
    description: 三河交匯後河道變寬，流速減緩，泥沙沉積形成廣袤沖積平原
  - target: aurum_river
    type: conceptual
    direction: 東方平行
    description: 奧魯姆河在東方平行入海，兩河之間是凱撒里克的核心農業區
  - target: wind_isles
    type: conceptual
    direction: 東方入海口
    description: 大河最終注入東部海洋，與風息群島共享同一海域
```

## 現實參考與想象指導

**河流分段特徵**（必須詳細描述，這是核心）：

| 河段 | 現實參考 | 特徵 |
|------|---------|------|
| **上游（西部高地）** | 長江上游、尼羅河上游 | 清澈湍急，峡谷深切，落差大，水聲如雷，魚類稀少但體型巨大 |
| **中游（沖積平原）** | 美索不達米亞、恆河平原 | 河道寬闊，水流緩慢，泥沙沉積，季節性氾濫，兩岸無數支流與沼澤 |
| **下游（東部平原）** | 尼羅河三角洲、長江三角洲 | 河道分叉，沙洲密布，鹹淡水交匯，漁業發達，蘆葦叢生 |
| **貫穿隘口段** | 長江三峽、科羅拉多峽谷 | 兩岸峭壁百米高，水流極速，漩渦與暗礁，只有經驗最豐富的船夫才能通過 |

**季節變化**：
- **春季**：上游融雪 + 世界樹樹雨 → 水位暴漲，「春汛」，沖積平原開始泛濫，帶來肥沃淤泥
- **夏季**：水位穩定，主河道可行大型貨船，兩岸灌溉渠全力運轉，農田綠浪翻滾
- **秋季**：水位漸退，露出沙洲與河灘，漁民在淺灘設置魚梁，候鳥沿河南下
- **冬季**：北段接近結冰（但約恩維德山脈阻擋了最冷空氣，所以僅北岸有薄冰），南段仍可通航

**人文**：
- 河上有無數渡口、水車磨坊、漁村、河盜據點
- 傑米努斯河是東西貿易的命脈，塞拉菲昂的糧食與凱撒里克的隕鐵經由水路運輸
- 魯普圖斯隘口段的船夫形成獨特的「峽谷行會」，世代相傳險灘航線的秘密
- 沖積平原段的農民每年秋季舉行「淤泥祭」，感謝河流帶來的肥沃土壤

## 感官細節指導（必須填寫 atmosphere）

- **scent**：上游的清冽礦物味、中游的泥沙與腐殖土、下游的鹹淡水混合腥味、隘口段的潮濕岩壁霉味、兩岸蘆葦的甜腥
- **light**：上游峡谷的幽綠水光折射、中游平原的開闊天光倒影、下游三角洲的夕照金紅、隘口段的狹窄一線天
- **temperature**：上游冰涼、中游溫和、下游受海洋影響偏暖、冬季北岸結冰南岸不結
- **sound**：上游的湍急轟鳴、中游的緩流低語、船槳划水聲、漁歌、河盜的警哨、水車的吱嘎

## Schema 提醒
- `layer: geography`
- `parent_id: ankora`
- `region: 中央`
- `empire`: `無`（跨帝國河流）
- 必填：`id`, `name`, `layer`, `region`, `empire`, `description`, `atmosphere`, `tags`
- 參考黃金範本：`SCHEMA.md` 第二節

## 輸出
寫入 `data/01-west-seraphion/geographies/flumen-geminus.yaml`
