# 子代理任務書：約恩維德山脈與約恩維德河（Jarnvid Mountains & River）

## 目標
建立兩個檔案：
1. `data/03-north-frost/geographies/northern-mountains.yaml`（約恩維德山脈，層級：`geography`）
2. `data/03-north-frost/geographies/jarnvid-river.yaml`（約恩維德河，層級：`geography`）

## 核心定位
**極北屏障**、**鐵森林**、**冷冽之源**。約恩維德山脈是安納克大陸最北端的屏障，也是諾德風格地理的核心。

## 已知事實（不可違背）
- 約恩維德山脈橫亙極北
- 北境諸邦的家園
- 約恩維德河發源於此，向南流淌，在沖積平原北側匯入傑米努斯大河
- 與怒嘯山脈在東北方向有連接（東北連綿山脈）
- 阻擋了極北冷空氣，使杰米努斯河北段冬季不至於完全結冰
- Jarnvid 意為「鐵森林」

## 與其他 Geography 的連接（山脈）

```yaml
connections:
  - target: the_howling_peaks
    type: physical
    direction: 東南方
    description: 東北連綿山脈與怒嘯山脈北端相接，形成大陸東北部的山弧
  - target: jarnvid_river
    type: physical
    direction: 南麓
    description: 冰川融水與山溪匯聚成約恩維德河，向南流淌
  - target: north_frost
    type: conceptual
    direction: 山脈以北與山間
    description: 北境諸邦散居於山脈北麓的冰原與峽灣之間
  - target: flumen_geminus
    type: conceptual
    direction: 南方
    description: 山脈阻擋極北冷空氣，使杰米努斯河北段冬季僅結薄冰，維持通航
```

## 與其他 Geography 的連接（河流）

```yaml
connections:
  - target: northern_mountains
    type: physical
    direction: 北段發源
    description: 發源於約恩維德山脈南麓的冰川與永凍層
  - target: the_howling_peaks
    type: conceptual
    direction: 南方流經
    description: 河流沿怒嘯山脈西麓南下，山脈融水不斷補給
  - target: flumen_geminus
    type: physical
    direction: 南端匯入
    description: 在沖積平原北側匯入傑米努斯大河，匯流處水色清冽與泥黃分明
  - target: the_flood_plain
    type: physical
    direction: 東岸
    description: 河流東岸是格蘭迪斯大公領地的北界，砂質土壤適合黑麥
```

## 現實參考與想象指導

**山脈參考**：斯堪的納維亞山脈（極光、峽灣、針葉林）+ 烏拉爾山脈（歐亞分界、礦產）+ 冰島高原（火山與冰川共存）+ 西伯利亞（永凍層、苔原）

**山脈分段特徵**：
- **北坡（極地側）**：終年冰雪覆蓋，冰川緩慢移動，冰裂隙深不可測。無植物，只有白色。
- **山腰（鐵森林區）**：Jarnvid 的命名由來——不是普通的森林，而是被隕鐵礦脈滲透的扭曲黑松林。樹幹呈現不自然的金屬光澤，樹脂帶有鐵鏽味。這裡是北境諸邦的聖地。
- **南坡（溫帶側）**：逐漸過渡為正常的針葉林與高山草甸，是北境諸邦的主要牧場與獵場。
- **峽灣與溫泉**：山脈西側（朝向未知海洋）有深邃的峽灣，某些谷地因地熱活動而終年不凍，形成「冰火之谷」。

**河流特徵**：
- 上游：冰川融水，清澈見底但冰冷刺骨，河床布滿被冰川磨圓的巨石
- 中游：流速減緩，兩岸是鐵森林的邊緣，水中帶有微量鐵鏽色
- 下游：進入平原，河水變寬變淺，冬季北岸結冰，中央仍有流動水道
- 特殊現象：每年春季「冰川潰決」——上游冰川湖突然潰堤，河水暴漲，沖毀下游堤壩

**人文**：
- 北境諸邦不是單一國家，而是散居於山脈與冰原間的部落聯盟
- 「鐵森林」是禁忌之地，傳說被隕鐵輻射扭曲的生物出沒其中
- 約恩維德河的春季潰決被視為山神的憤怒，部落會在河岸獻祭
- 北境的獵人會沿河南下，到沖積平原的市集交換毛皮與琥珀

## 感官細節指導（山脈）

- **scent**：極北的空虛無味、鐵森林的樹脂與鐵鏽混合味、溫泉谷地的硫磺、冰裂隙的古老壓縮空氣
- **light**：極晝的慘白、極夜的漆黑與極光（綠與紫的舞動）、鐵森林中樹幹的金屬微光反射
- **temperature**：極寒（主峰）→ 寒冷（山腰）→ 涼爽（南坡）
- **sound**：冰川移動的深層轟鳴（地底感）、永恆風嘯、冰裂隙的爆裂聲、溫泉的氣泡咕嚕、鐵森林中樹脂滴落的清脆

## 感官細節指導（河流）

- **scent**：上游的清冽無味、中游的鐵鏽與松脂、下游的濕土與腐殖質
- **light**：上游的冰川藍（水中懸浮的冰晶折射）、中游的幽綠（鐵森林蔭蔽）、下游的泥黃與天空倒影
- **temperature**：全年冰涼，夏季亦不超過十度，冬季接近結冰
- **sound**：上游的湍急與巨石撞擊、中游的緩流低語、春季潰決時的毀滅性轟鳴、冬季薄冰下的暗流

## Schema 提醒
- `layer: geography`
- `parent_id: ankora`
- `region`: 山脈填 `北部`，河流填 `北部`
- `empire`: 山脈填 `北境諸邦`（或 `無`，因為是部落散居），河流填 `無`
- 必填：`id`, `name`, `layer`, `region`, `empire`, `description`, `atmosphere`, `tags`
- 參考黃金範本：`SCHEMA.md` 第二節

## 輸出
寫入兩個檔案：
- `data/03-north-frost/geographies/northern-mountains.yaml`
- `data/03-north-frost/geographies/jarnvid-river.yaml`
