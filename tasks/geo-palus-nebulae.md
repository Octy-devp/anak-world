# 任務書：帕魯斯沼澤（Palus Nebulae，迷霧沼澤）

## 目標
建立 `/workspaces/anak-world/data/01-west-seraphion/geographies/palus-nebulae.yaml`

## 精確空間定位

迷霧沼澤位於**中央沖積平原北緣**，傑米努斯河中游一條季節性支流的終點低洼地帶。

**與現有地理實體的相對位置**：
- **南方**：中央沖積平原（the_flood_plain）的北端——沼澤是沖積平原與北部丘陵之間的過渡帶
- **北方**：怒嘯山脈西麓的丘陵緩坡——雨水與融雪經丘陵滲流後匯入沼澤
- **東方**：傑米努斯河（flumen_geminus）中游主河道——沼澤的水源之一來自傑米努斯河的季節性氾濫
- **西方**：格蘭迪斯大公國的麥田邊緣——農民開墾到沼澤邊緣就停止，因為排水成本過高
- **氣候**：冬季濕冷多霧，夏季悶熱、蚊蟲滋生、瘴氣瀰漫

## 地緣政治邊界（紅線）

- **帕魯斯沼澤位於塞拉菲昂神聖帝國境內**，不是國際邊界。
- 它是帝國內部的「**行政邊緣地帶**」——位於格蘭迪斯大公國（北方）與五大特別市聯盟（南方）之間的交界模糊區。兩邊都宣稱管轄權，但實際上都不願投入資源治理。
- **禁止**：不要把沼澤設定為「東西帝國之間的走私通道」。東西帝國之間已有怒嘯山脈和魯普圖斯隘口作為主要通道。帕魯斯沼澤是**帝國內部**不同勢力（格蘭迪斯 vs 特別市聯盟 vs 教廷）之間的灰色地帶。
- **教廷控制力薄弱**：沼澤地帶不適合建造教堂與修道院，因此普世教會西派的影響力較弱，這使得異端、走私者、逃犯得以藏身。

## 故事功能

1. **內部灰色地帶**：帕魯斯沼澤是塞拉菲昂帝國內部的「法外之地」。格蘭迪斯的麥穗軍團不願進入，教廷的巡察僧視其為不潔之地，五大特別市的商人則利用沼澤小徑避開關稅站。
2. **瘟疫與瘴氣**：夏季的沼澤瘴氣被教廷解讀為「阿薩對異端的懲罰」，但實際上是自然的水文現象。這種解讀本身就構成了敘事張力（宗教 vs 自然科學）。
3. **古代遺跡**：大洪水前的青銅時代，傑米努斯河的河道曾經過此處，留下了被淹沒的古代村落與堤壩遺跡（與現有的 `dam_ruins_outpost` 和 `ruina_damni` 形成地理關聯）。

## 必須建立的 Connections

```yaml
connections:
  - target: the_flood_plain
    type: physical
    direction: 南方
    description: 沼澤是中央沖積平原北緣的低洼過渡帶，雨季時兩者幾乎連為一體
  - target: flumen_geminus
    type: physical
    direction: 東方
    description: 傑米努斯河的一條季節性支流在沼澤東緩緩沒入濕地，夏季氾濫時倒灌
  - target: the_howling_peaks
    type: physical
    direction: 北方
    description: 怒嘯山脈西麓丘陵的滲流水經地下徑流匯入沼澤
  - target: molinaria
    type: conceptual
    direction: 東南方
    description: 磨坊鎮位於傑米努斯河主河道旁，與沼澤之間的農田帶是格蘭迪斯大公國的開墾前線
  - target: ruina_damni
    type: conceptual
    direction: 西方
    description: 古代堤壩遺跡與沼澤中的被淹沒遺跡屬於同一青銅時代水利工程系統
```

## 規範
- `id`: `palus_nebulae`
- `layer`: `geography`
- `region`: 中央/西部
- `empire`: 塞拉菲昂神聖帝國（行政歸屬模糊，格蘭迪斯與特別市聯盟都宣稱管轄）
- `parent_id`: `ankora`
- 參考範本：`/workspaces/anak-world/data/01-west-seraphion/geographies/the-howling-peaks.yaml`
- `atmosphere` 必須完整
- 非 source 直接描述標註 `# inferred: true`

## 命名
- 拉丁：Palus Nebulae（迷霧之沼）
- 中文：帕魯斯沼澤 或 迷霧沼澤
