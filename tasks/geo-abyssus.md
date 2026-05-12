# 子代理任務書：阿比蘇斯大無底洞（The Abyssus）

## 目標
建立 `data/05-secret-eldara/geographies/the-abyssus.yaml`（層級：`geography`）

## 已知事實（不可違背）
- 阿比蘇斯大無底洞位於大陸南部，塔爾塔魯斯山脈以南
- 目前無人知曉其底部，是一個「謎」
- 隕鐵與失傳技術的源頭
- 南部塔爾塔魯斯山脈隔開了已知世界與大無底洞
- 塔爾塔魯斯暗河（Tartarus Stream）流向大無底洞
- 怒嘯山脈南端通過斷斷續續的小山脈鏈接到塔爾塔魯斯山脈
- 約恩維德山脈在極北，與深淵形成大陸南北兩極的對稱

## 與其他 Geography 的連接（必須寫入 connections）

```yaml
connections:
  - target: the_howling_peaks
    type: conceptual
    direction: 北方
    description: 南端山脈鏈與塔爾塔魯斯山脈地質同源，皆為大洪水時期的地殼傷疤
  - target: southern_mountains
    type: physical
    direction: 北界
    description: 塔爾塔魯斯山脈是深淵與已知世界的最後屏障
  - target: tartarus_stream
    type: physical
    direction: 北方匯入
    description: 暗河從山脈滲入深淵，傳說在底部形成地下海
  - target: eldara_worldtree
    type: conceptual
    direction: 對立
    description: 深淵代表死亡與失傳的毀滅技術，世界樹代表生命與自然魔法，兩者通過地下水系形成微妙的能量平衡
```

## 現實參考與想象指導

**地質**：參考西伯利亞通古斯撞擊坑（超規模）+ 東非大裂谷（地殼撕裂）+ 冰島裂谷（地熱與硫磺）+ 瑪雅天坑（cenote，通往地下世界的儀式入口）。但規模放大一千倍。

**核心設定**：深淵不是普通的峽谷或火山口，而是「大陸的傷口」——大洪水時期隕鐵撞擊或地殼被撕裂的結果。深淵邊緣的岩石呈現不自然的紫黑色，帶有金屬光澤（隕鐵礦脈暴露）。

**氣候影響**：深淵持續釋放地熱與硫磺氣體，在塔爾塔魯斯山脈南麓形成局部的「熱霾區」——即使在冬季，山腳某些谷地也終年溫暖，生長著不應存在的熱帶植物。這種異常氣候被當地人視為惡魔的氣息。

**生態（深淵邊緣）**：
- 發光真菌與苔藓（利用地熱與硫化氫進行化能合成）
- 無眼的白色生物（適應黑暗）
- 變異的植物（受隕鐵輻射影響）

**人文**：
- 黑曜石守望者（Obsidian Watchers）守護深淵邊緣，阻止凡人進入
- 盜礦者與冒險家冒死攀下深淵採集隕鐵碎片
- 深淵邊緣的廢棄營地與絞架（警示後來者）

## 感官細節指導（必須填寫 atmosphere）

- **scent**：硫磺與腐蛋味、燒焦金屬的刺鼻、深淵底部飄上來的潮濕霉味、熱霾區的異常花香（不應存在的熱帶植物）
- **light**：深淵內部是絕對的漆黑，只有邊緣發光真菌的幽綠微光、熱霾區的扭曲光線折射
- **temperature**：深淵邊緣因地熱而溫熱，越往下越熱（與常理相反）
- **sound**：深淵底部傳來的低頻嗡鳴（有人說是地下海的潮汐，有人說是某種巨獸的呼吸）、風吹過深淵的尖嘯、發光真菌的輕微爆裂聲

## Schema 提醒
- `layer: geography`
- `parent_id: ankora`
- `region: 南部`
- 必填：`id`, `name`, `layer`, `region`, `empire`, `description`, `atmosphere`, `tags`
- `empire` 字段：填 `無`（不屬於任何帝國）
- `properties.access_level` 建議 `secret`（極度危險，禁止進入）
- `properties.danger_level` 建議 `deadly`
- 參考黃金範本：`SCHEMA.md` 第二節的 YAML 結構

## 輸出
寫入 `data/05-secret-eldara/geographies/the-abyssus.yaml`
