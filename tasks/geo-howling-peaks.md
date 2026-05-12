# 子代理任務書：怒嘯山脈（The Howling Peaks）

## 目標
建立 `data/01-west-seraphion/geographies/the-howling-peaks.yaml`（層級：`geography`）

## 已知事實（不可違背）
- 怒嘯山脈縱貫大陸中央，南北走向，如巨龍脊骨隔開東西兩大帝國
- 傑米努斯大河（Flumen Geminus）東西貫穿其間的**魯普圖斯隘口**（Ruptus Pass）
- 東北有連綿山脈連接到中央，然後斷斷續續的小山脈鏈接到南部塔爾塔魯斯山脈
- 大陸呈南北走向
- 沖積平原在山脈以西（塞拉菲昂境內），是糧食核心產區
- 北境是約恩維德山脈（Jarnvid），北境諸邦的家園
- 塞拉菲昂在山西側，凱撒里克在山東側

## 與其他 Geography 的連接（必須寫入 connections）

```yaml
connections:
  - target: ruptus_pass
    type: physical
    direction: 中央段
    description: 傑米努斯河切穿山脈的唯一隘口，東西陸路通道
  - target: the_abyssus
    type: conceptual
    direction: 南端
    description: 南端斷續山脈鏈與塔爾塔魯斯山脈地質同源，皆為大洪水時期的地殼傷疤
  - target: eldara_worldtree
    type: physical
    direction: 西麓
    description: 西麓融雪與地下水系滋養世界樹根系
  - target: flumen_geminus
    type: physical
    direction: 貫穿
    description: 河流從魯普圖斯隘口東西貫穿山脈
  - target: jarnvid_river
    type: physical
    direction: 北麓
    description: 約恩維德河發源於山脈北麓，向北流淌
```

## 現實參考與想象指導

**地質**：參考安第斯山脈（縱貫大陸、分隔兩側文明）+ 喜馬拉雅（高聳、宗教聖地）+ 落基山脈（富含礦脈）。山體富含**隕鐵礦脈**（安納克文明的技術基礎），大洪水時期地殼撕裂形成的褶皺山脈。

**氣候與生態**：
- 西坡（塞拉菲昂側）：**緩坡**，接受西風帶來的海洋濕氣，形成高山草甸與針葉林，山腳過渡為溫帶闊葉林
- 東坡（凱撒里克側）：**陡坡**，背風乾燥，岩石裸露，風蝕嚴重
- 海拔梯度：山腳闊葉林 → 山腰針葉林 → 雪線高山草甸 → 主峰永久冰川
- 雪線約在海拔 3500 米

**人文**：
- 魯普圖斯隘口有走私通道和邊境稅站
- 山中有隕鐵礦場、修道院（隱修士躲避世俗戰亂）、瞭望塔
- 傳說山脈是巨龍脊骨所化

## 感官細節指導（必須填寫 atmosphere）

- **scent**：高海拔的稀薄冷冽空氣、針葉林的松脂、西坡腐殖土與野花、東坡風蝕岩石的粉塵味、隘口處的馬匹與鐵鏽味
- **light**：西坡晨曦與夕照金紅，東坡陰影中的冷藍反光，雪線以上的刺眼白茫
- **temperature**：山腳溫帶涼爽 → 山腰寒冷 → 主峰極寒
- **sound**：永恆風嘯（山脈得名由來）、融雪溪流的湍急、隘口商隊的鈴鐺、東坡風蝕岩的尖嘯

## Schema 提醒
- `layer: geography`
- `parent_id: ankora`
- `region: 中央`
- 必填：`id`, `name`, `layer`, `region`, `empire`, `description`, `atmosphere`, `tags`
- `empire` 字段：雖然山脈跨兩大帝國，但 YAML 是單一地點，填 `無` 或 `爭議`
- `properties.access_level` 建議 `restricted`（山脈險峻，非普通人可穿越）
- 參考黃金範本：`SCHEMA.md` 第二節的 YAML 結構

## 輸出
寫入 `data/01-west-seraphion/geographies/the-howling-peaks.yaml`
