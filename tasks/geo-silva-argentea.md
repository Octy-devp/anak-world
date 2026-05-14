# 任務書：西爾瓦阿根泰亞（Silva Argentea，銀葉林）

## 目標
建立 `/workspaces/anak-world/data/01-west-seraphion/geographies/silva-argentea.yaml`

## 精確空間定位

銀葉林位於**安納克大陸西南部**，是塞拉菲昂神聖帝國與艾爾達拉秘境之間的廣闊溫帶-亞寒帶森林帶。

**與現有地理實體的相對位置**：
- **西方**：艾爾達拉世界樹（eldara_worldtree）的森林邊緣——銀葉林的西端與世界樹森林的東端之間沒有明確界線，而是漸變的「森民領地」
- **東方**：塞拉菲昂帝國的農耕區與拉迪克斯守望修道院（radix_specula）所在的邊境防線
- **北方**：席爾瓦因河（sylvaine_river）流經森林北緣，形成自然邊界
- **南方**：塔爾塔魯斯山脈（southern_mountains）北麓的丘陵地帶
- **氣候**：受世界樹魔法影響，森林內部比同緯度地區更溫暖濕潤；秋季時銀白色樹葉（白楊/樺樹混交）形成壯觀景觀

## 地緣政治邊界（紅線）

- **森民（席爾凡）完全隔離**：這是絕對原則。銀葉林的深處（西部）是森民領地，人類禁止進入。東部邊緣是人類伐木區與邊境巡邏路線。
- **禁止設定混居**：不能有「人類與森民共處的村莊」、「混血聚落」、「秘密交易市場」等。
- **人類活動範圍**：僅限於森林東緣 20-30 里內的伐木區、獵人小徑、邊境巡邏路線。超過此範圍即為森民領地，進入者失蹤。
- **邊境防線**：塞拉菲昂在東緣設有一系列哨站（以拉迪克斯守望修道院為中心），但這些哨站不是為了「進攻」森民，而是為了「監控」與「阻止人類誤入」。
- **禁止**：不要把銀葉林設定為「教廷與森民的戰場」或「雙方爭奪的領土」。森民與人類之間是隔離，不是戰爭。

## 故事功能

1. **緩衝帶與神秘邊界**：銀葉林是「已知世界」與「未知世界」之間的灰色過渡帶。人類伐木工在東緣聽到西邊傳來奇異歌聲，但從未見過歌者。
2. **走私與異端通道**：雖然森民與人類不直接接觸，但森林的複雜地形使得某些人類走私者利用東緣小徑避開官方商道——他們不走得太深，但利用森林掩護。
3. **魔法退化的對比**：世界樹森林的魔法仍然活躍，而銀葉林東緣的魔法已經退化，這種梯度構成了有趣的敘事對比。

## 必須建立的 Connections

```yaml
connections:
  - target: eldara_worldtree
    type: physical
    direction: 西方深處
    description: 銀葉林的西端漸變為世界樹森林，森民領地自此開始，人類禁止進入
  - target: sylvaine_river
    type: physical
    direction: 北方
    description: 席爾瓦因河沿森林北緣流淌，是銀葉林與北方平原的自然分界
  - target: southern_mountains
    type: physical
    direction: 南方
    description: 塔爾塔魯斯山脈北麓的丘陵地帶構成銀葉林的南部邊界
  - target: radix_specula
    type: conceptual
    direction: 東方邊境
    description: 拉迪克斯守望修道院位於森林東緣，監控森民動向並阻止人類誤入
```

## 規範
- `id`: `silva_argentea`
- `layer`: `geography`
- `region`: 西南部
- `empire`: 塞拉菲昂神聖帝國（東緣）；艾爾達拉秘境（西緣深處）
- `parent_id`: `ankora`
- 參考範本：`/workspaces/anak-world/data/01-west-seraphion/geographies/the-howling-peaks.yaml`
- `atmosphere` 必須完整
- 非 source 直接描述標註 `# inferred: true`

## 命名
- 拉丁：Silva Argentea（銀色的森林）
- 中文：西爾瓦阿根泰亞 或 銀葉林
