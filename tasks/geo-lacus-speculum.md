# 任務書：斯佩庫拉湖（Lacus Speculum，鏡湖）

## 目標
建立 `/workspaces/anak-world/data/01-west-seraphion/geographies/lacus-speculum.yaml`

## 精確空間定位

鏡湖位於**怒嘯山脈北麓**與**約恩維德山脈南端**的交會高地，是安納克大陸中部偏北的一座高山冰蝕湖。

**與現有地理實體的相對位置**：
- **北方**：約恩維德山脈（northern_mountains）的南端余脈
- **南方**：怒嘯山脈（the_howling_peaks）的北麓雪線
- **東方**：傑米努斯大河（flumen_geminus）上游峽谷，湖水經地下溶洞與融雪補給傑米努斯河
- **西方**：北境諸邦的霍羅托里亞高原遠景（不可直達，中間有山脈阻隔）
- **海拔**：約 2000-2500 米，冬季完全冰封，夏季冰緣消退

## 地緣政治邊界（紅線）

- **鏡湖位於塞拉菲昂神聖帝國境內**，不是國際邊界。
- 但它靠近帝國北部邊境，是西爾伯弗羅斯特邊疆大公國的北部水源補給區。
- 北境諸邦（north_frost）的霜生部落偶爾在冬季越過約恩維德山脈南麓的薄弱點，接近鏡湖區域——這構成了邊境緊張，但不是正式的領土爭議。
- **禁止**：不要把鏡湖設定為「塞拉菲昂與北境的邊界湖泊」或「兩國共享湖泊」。它是塞拉菲昂境內的高山湖，但受到北方威脅。

## 故事功能

1. **水源戰略**：鏡湖是傑米努斯河上游的重要補給源。控制了鏡湖，就控制了下游維特魯斯與中央沖積平原的夏季水量。
2. **預言/幻象傳說**：湖面在特定季節（春分、秋分）的黎明時分，會因高海拔稀薄空氣與冰晶折射產生複雜的光學現象，被當地修士解讀為「阿薩的預言」。
3. **邊境緊張的舞台**：西爾伯弗羅斯特的邊境巡邏隊與北境霜生獵人在湖區周邊的隱蔽衝突。

## 必須建立的 Connections

```yaml
connections:
  - target: the_howling_peaks
    type: physical
    direction: 南方
    description: 鏡湖坐落於怒嘯山脈北麓的高山谷地中
  - target: northern_mountains
    type: physical
    direction: 北方
    description: 約恩維德山脈南端的余脈環繞湖泊北岸
  - target: flumen_geminus
    type: physical
    direction: 東南方
    description: 湖水經地下溶洞與夏季融雪補給傑米努斯河上游支流
  - target: jarnvid_river
    type: physical
    direction: 北方
    description: 約恩維德河的一條小支流發源於湖泊東側的冰蝕谷
```

## 規範
- `id`: `lacus_speculum`
- `layer`: `geography`
- `region`: 北部/中央交界
- `empire`: 塞拉菲昂神聖帝國（西爾伯弗羅斯特邊疆大公國實際控制區域）
- `parent_id`: `ankora`
- 參考範本：`/workspaces/anak-world/data/01-west-seraphion/geographies/the-howling-peaks.yaml`
- `atmosphere` 必須完整（scent, light, temperature, sound）
- 非 source 直接描述標註 `# inferred: true`

## 命名
- 拉丁：Lacus Speculum（鏡湖）
- 中文：斯佩庫拉湖 或 鏡湖
