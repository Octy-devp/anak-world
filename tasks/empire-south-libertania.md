# 子代理任務書：自由城邦聯盟（Libertania）

## 目標
建立 `data/04-south-libertania/empire.yaml`（層級：`empire`）

## 核心定位
**自由的燈塔**。一個由海上商業城邦組成的聯邦，用金幣取代了神恩券，證明了「沒有教會的社會也可以繁榮」。

## 已知事實（來自原文，不可違背）

**前身**：利貝塔尼亞（Libertania），原安納克自由聯邦

**組成**：風息群島的七個商業城邦（已在 geography YAML 中詳細描述）

**政治體制**：
- 漢撒同盟、威尼斯、熱那亞的混合聯邦制
- 各城邦以「薩穆德拉盟誓」（Samudra Pact）維繫
- 沒有常備軍，只有季風來臨時集結的帆隊聯防
- 風息議會（Windbreath Council）作為協商機構

**歷史關鍵事件**：
- 第754年：《大憲章》簽訂時，利貝塔尼亞代表拒絕簽字，理由是「自由城邦不受封建契約約束」
- 第775年：正式宣布脫離塞拉菲昂帝國
- 「風役護照」制度：服役三年獲公民權與土地

**經濟**：
- 壟斷南方海鹽、珍珠、珊瑚與香料貿易
- 用利貝塔尼亞金幣取代塞拉菲昂的神恩券
- 到第800年，人均財富已超過維特魯斯
- 提供「替代選項」——不滿封建壓迫者可乘船前往風息群島

**宗教**：
- 信奉「風母與七洋靈」的泛靈信仰
- 每艘商船出航前獻上香料與珊瑚粉
- 務實的海洋文化，「不崇拜任何神祇，只信奉契約與風向」

**與塞拉菲昂的關係**：
- 第800年後與塞拉菲昂關係緊張
- 塞拉菲昂的海軍試圖封鎖風息群島，但城邦的輕快帆船與隕鐵加固艦隊使封鎖效果有限

**地理關聯**：
- 奧魯姆河出海口外海的群島
- 東南方海域
- 與凱撒里克帝國東南方臨海

## 與 Geography 的連接（必須寫入 connections）

```yaml
connections:
  - target: wind_isles
    type: physical
    direction: 核心領土
    description: 風息群島是自由城邦聯盟的全部領土，七城邦組成聯邦核心
  - target: aurum_river
    type: physical
    direction: 西北方
    description: 奧魯姆河出海口是群島與大陸的主要聯繫通道
  - target: the_abyssus
    type: conceptual
    direction: 西方遠海
    description: 某些老水手聲稱在群島最南端暴風夜可聽到深淵的低頻嗡鳴
```

## Schema 提醒
- `layer: empire`
- `parent_id: ankora`
- `region: 東南部`
- `empire`: `無`
- 必填：`id`, `name`, `layer`, `region`, `empire`, `description`, `atmosphere`, `tags`

## 感官細節指導
- **scent**：全年鹽風、混合香料、松脂焦油、珊瑚與海藻、異國貨幣的金屬味
- **light**：熱帶強光與銳利陰影、潟湖波光、夕照金紅、夜間藍眼淚
- **temperature**：常年濕熱無冬，季風時涼爽，午後雷陣雨
- **sound**：帆索噼啪、多國語言喧囂、潮汐漲退、風息議會的風鳴、遠方暴風雨雷鳴

## 輸出
寫入 `data/04-south-libertania/empire.yaml`
