# 子代理任務書：塔爾塔魯斯山脈與暗河（Tartarus Mountains & Stream）

## 目標
建立兩個檔案：
1. `data/05-secret-eldara/geographies/southern-mountains.yaml`（塔爾塔魯斯山脈，層級：`geography`）
2. `data/05-secret-eldara/geographies/tartarus-stream.yaml`（塔爾塔魯斯暗河，層級：`geography`）

## 核心定位
**深淵的門檻**、**地熱之牆**、**死亡屏障**。塔爾塔魯斯山脈是已知世界的最南端邊界，也是大陸與深淵之間的最後防線。

## 已知事實（不可違背）
- 位於大陸南部，隔開已知世界與阿比蘇斯大無底洞
- 與怒嘯山脈南端通過斷斷續續的小山脈鏈接
- 山脈以南即為大無底洞
- 塔爾塔魯斯暗河從山脈滲入深淵
- 深淵持續釋放地熱與硫磺，在山脈南麓形成「熱霾區」
- 即使在冬季，山腳某些谷地也終年溫暖，生長著不應存在的熱帶植物
- 山脈岩石呈現不自然的紫黑色，帶有金屬光澤（隕鐵暴露）

## 與其他 Geography 的連接（山脈）

```yaml
connections:
  - target: the_howling_peaks
    type: conceptual
    direction: 北方
    description: 南端斷續山脈鏈與怒嘯山脈地質同源，皆為大洪水時期的地殼傷疤
  - target: the_abyssus
    type: physical
    direction: 南方
    description: 山脈是深淵與已知世界的最後屏障，某些峭壁上可見深淵邊緣的紫黑色岩石
  - target: tartarus_stream
    type: physical
    direction: 山體內部
    description: 無數地下暗河從山脈滲入，匯聚成塔爾塔魯斯暗河，最終墜入深淵
  - target: wind_isles
    type: conceptual
    direction: 東南方
    description: 山脈東南麓的熱霾區與風息群島的熱帶氣候可能有关联（深淵地熱的遠程影響）
```

## 與其他 Geography 的連接（暗河）

```yaml
connections:
  - target: southern_mountains
    type: physical
    direction: 發源地
    description: 無數地下支流從塔爾塔魯斯山脈的裂縫與溶洞中滲出，匯聚成主暗河
  - target: the_abyssus
    type: physical
    direction: 終點
    description: 暗河在深淵邊緣墜入虛空，傳說在深淵底部形成地下海，水聲從下方迴盪而上
  - target: eldara_worldtree
    type: conceptual
    direction: 對立
    description: 暗河是死亡與腐蝕之水，與世界樹的希爾薇恩河（生命之水）形成地下水的陰陽兩極
```

## 現實參考與想象指導

**山脈參考**：安第斯火山帶（地熱與硫磺）+ 埃塞俄比亞高地（裂谷與高原）+ 冰島（火山與冰川並存）+ 黃石公園（地熱活動）

**山脈分段特徵**：
- **北坡（朝向平原側）**：乾燥荒涼，岩石裸露，植被稀疏。這裡是深淵影響的過渡帶，空氣中瀰漫淡淡的硫磺味。
- **山腰（地熱活躍區）**：溫泉、間歇泉、硫磺噴口遍佈。某些谷地因地熱而終年溫暖，形成「熱霾谷」——不應存在的熱帶植物在此瘋長，與周圍的荒涼形成詭異對比。
- **南坡（朝向深淵側）**：絕對的死寂。沒有植物，沒有昆蟲，只有紫黑色的岩石和地熱蒸汽。空氣中氧氣稀薄，帶有劇毒氣體。
- **主峰**：被稱為「守望者之座」，黑曜石守望者的最南哨站設於此。

**暗河特徵**：
- 不是單一河流，而是無數地下支流匯聚的網絡
- 水流在絕對黑暗中流淌，只有發光真菌提供微弱照明
- 水質富含硫磺與礦物質，呈現詭異的乳白色，接觸皮膚會造成灼傷
- 河道中有地下瀑布與巨型溶洞，某些地方的洞頂高達百米
- 暗河最終在深淵邊緣的「哭泣峭壁」墜入虛空，水聲如萬人齊哭

**生態（熱霾谷）**：
- 地熱溫泉中的嗜熱藻類形成粉紅色池塘
- 變異的蕨類與藤蔓（受隕鐵輻射影響）
- 無眼的白色甲蟲與洞穴魚類
- 某些植物會在夜間發出微弱的藍光（生物發光）

**人文**：
- 幾乎無人居住，只有黑曜石守望者的哨站
- 盜礦者冒死穿越山脈，到深淵邊緣採集隕鐵碎片
- 熱霾谷中的變異植物被煉金術士視為珍貴材料
- 傳說暗河深處有通往「地下世界」的入口

## 感官細節指導（山脈）

- **scent**：北坡的乾燥塵土、山腰的硫磺與溫泉蒸汽、南坡的劇毒氣體與燒焦金屬、熱霾谷的異常花香（甜膩到令人作嘔）
- **light**：北坡的蒼白天光、山腰的溫泉蒸汽折射出的彩虹、熱霾谷的扭曲光線、南坡的無光黑暗（只有深淵方向的幽綠微光）
- **temperature**：北坡炎熱乾燥、山腰溫暖潮濕（溫泉區）、南坡灼熱（地熱）、冬季不受影響（地熱持續）
- **sound**：間歇泉的噴發轟鳴、地下蒸汽的嘶嘶聲、岩石因熱脹冷縮的爆裂、暗河墜入深淵的遙遠轟鳴、熱霾谷中變異植物的夜間發光嗡嗡聲

## 感官細節指導（暗河）

- **scent**：地下空間的潮濕霉味、硫磺的刺鼻、礦物質的金属腥甜、深淵方向的腐敗氣息
- **light**：絕對黑暗，僅有發光真菌的幽綠、某些礦物的微弱磷光、暗河瀑布的水花折射
- **temperature**：恆溫潮濕，比地表溫暖（地熱影響），越接近深淵越熱
- **sound**：地下水的迴盪、瀑布的轟鳴、水滴落下的清脆（巨大空間中的微小聲音）、遠方深淵的低頻嗡鳴透過岩層傳來

## Schema 提醒
- `layer: geography`
- `parent_id: ankora`
- `region`: 山脈填 `南部`，暗河填 `南部`
- `empire`: 都填 `無`
- 山脈 `danger_level`: `high`
- 暗河 `danger_level`: `deadly`
- 必填：`id`, `name`, `layer`, `region`, `empire`, `description`, `atmosphere`, `tags`
- 參考黃金範本：`SCHEMA.md` 第二節

## 輸出
寫入兩個檔案：
- `data/05-secret-eldara/geographies/southern-mountains.yaml`
- `data/05-secret-eldara/geographies/tartarus-stream.yaml`
