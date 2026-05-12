# 子代理任務書：艾爾達拉秘境（Secret Eldara）

## 目標
建立 `data/05-secret-eldara/empire.yaml`（層級：`empire`）

## 核心定位
**不屬於任何凡俗政權的唯美隱世國度**。世界樹艾爾達拉的根系所在，森民（席爾凡）的家園，一片被迷霧結界封閉的傳說之地。

## 已知事實（來自原文，不可違背）

**統治者**：席爾瓦裡翁（Silverleaf Concord）— 母系血統為基礎的貴族長老制社會

**居民**：森民（Sylvans），外族稱之為精靈或 Elf
- 銀白色長髮與尖耳，肌膚如月光下的瓷器般剔透
- 不追求擴張與征服，以「唯美與永恆」為至高信條
- 魔法來自與世界樹的「共鳴」— 流水、烈焰、大地、疾風四大元素聽從召喚
- 拒絕金屬工具，認為隕鐵是「深淵的毒」
- 使用「生長工藝」而非鍛造

**首都/核心**：水晶宮廷（Crystal Court）— 世界樹根系與礦脈共鳴生長出的水晶樹脂結構

**歷史關鍵事件**：
- 大洪水時期：倖存者蜷縮於世界樹蔭庇之下
- 第483年：費羅斯誓約，森民首次大規模與人類合作對抗霜生
- 第485年：極北會戰，希爾薇恩化身銀葉聖樹
- 第490年：「大隱遁」（The Great Seclusion），迷霧結界封閉艾特恩瓦爾德森海
- 第582年：普世教會頒布《花園論》，將森民定義為「主神的謙卑從神」
- 第682年：教廷進一步將森民魔法納入「神恩」體系

**與人類的關係**：
- 緊鄰塞拉菲昂神聖帝國西南邊境，關係緊張
- 帝國覬覦森林資源，森民拒絕人類進入
- 邊境有迷霧結界，讓入侵者迷失方向
- 人類法師的元素魔法被視為從森民獲得的「特許權柄」

**現狀（第825年）**：
- 迷霧結界仍然存在，森民退回深處
- 極少數森民留在結界邊緣
- 艾特恩瓦爾德森海成為傳說，森民成為神話中的存在

**地理關聯**：
- 大陸西南部
- 緊鄰塞拉菲昂神聖帝國西南邊境
- 再西南部無人知曉
- 希爾薇恩河從森林流向傑米努斯大河

## 與 Geography 的連接（必須寫入 connections）

```yaml
connections:
  - target: eldara_worldtree
    type: physical
    direction: 核心
    description: 世界樹艾爾達拉是秘境的全部，森民與之共生
  - target: the_howling_peaks
    type: physical
    direction: 東方
    description: 怒嘯山脈西麓的融雪滋養世界樹根系
  - target: sylvaine_river
    type: physical
    direction: 東北方
    description: 希爾薇恩河從森林流向傑米努斯大河，是與外界的唯一自然通道
  - target: the_abyssus
    type: conceptual
    direction: 對立
    description: 世界樹代表生命與自然魔法，深淵代表死亡與毀滅技術
  - target: west_seraphion
    type: conceptual
    direction: 東北方
    description: 與塞拉菲昂帝國的邊境關係緊張，迷霧結界阻止入侵
```

## Schema 提醒
- `layer: empire`
- `parent_id: ankora`
- `region: 西南部`
- `empire`: `無`
- 必填：`id`, `name`, `layer`, `region`, `empire`, `description`, `atmosphere`, `tags`
- 注意：這不是人類帝國，而是異種族的隱世國度，需要在 description 中明確區分

## 感官細節指導
- **scent**：樹脂與松針的甜膩、腐殖土與蘑菇的濕潤、水晶的礦物清冽、霧雨的無味清新
- **light**：黎明淡金光束、正午翠綠濾光、月夜銀藍微光、永恆薄霧的夢幻散射
- **temperature**：恆溫濕潤，冬暖夏涼，樹雨帶來的涼意
- **sound**：樹葉沙沙細語（世界樹的低語）、根系緩慢生長、樹雨敲打水晶、遠方邊境巡邏隊的號角（不協和音）

## 輸出
寫入 `data/05-secret-eldara/empire.yaml`
