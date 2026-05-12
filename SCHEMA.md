# Ankora-World YAML Schema 規範

> **版本**：v0.2  
> **用途**：定義 `data/` 下所有 YAML 檔案的欄位、型別與填充規則（地點 + 勢力）。  
> **原則**：靜態優先、層次錨定、感官即索引、關係即通道。

---

## 一、六級層次（The Six Tiers）

每個 YAML 實體必須明確屬於以下六級之一：

| 層級 | 英文名 | 說明 | 範例 |
|------|--------|------|------|
| 大陸 | `continent` | 整個安納克大陸 | Ankora |
| 地理 | `geography` | 自然或宏觀地理實體（山脈、河流、深淵、森林、世界樹） | The Howling Peaks, Eldara, Abyssus |
| 帝國 | `empire` | 政治實體、國家、帝國 | Seraphion Empire |
| 定居點 | `settlement` | 城鎮、村莊、要塞、修道院等一切人類聚落 | Vetustapolis |
| 區域 | `district` | 定居點內的行政或功能區塊 | Inner City, Harbor District |
| 房間 | `room` | 可進入的具體空間，最小單位 | Sacred Key Complex, Throne Hall |
| **勢力** | **`faction`** | **非國家組織：傭兵團、行會、宗教結社、秘密組織、貿易聯盟** | **Frostblade Company, Ochre Guild** |

> **規則**：
> - `room` 必須有 `parent_id` 指向所屬 `district`
> - `district` → `settlement` → `empire` → `continent`
> - `geography` 可獨立存在，或作為其他地點的空間背景（如定居點位於山脈東麓）
> - `geography` 的 `parent_id` 通常指向 `continent`，也可指向另一 `geography`（如「龍脊隘口」屬於「怒嘯山脈」）
> - **`faction` 可獨立存在，不屬於任何地點層級；通過 `influence[]` 描述其在各地點的活動**

---

## 二、單一地點 YAML 結構

```yaml
# ── 身份錨定（必填）──
id: sacred_key_complex           # 全局唯一識別碼，snake_case，不可變
name: 聖鑰院複合體               # 人類可讀名稱
layer: room                      # [continent|empire|settlement|district|room]
region: 內城區                    # 所屬區域名稱
empire: 塞拉菲昂神聖帝國          # 所屬帝國名稱
parent_id: inner_city            # 上一層級的 id（continent 可省略）

# ── 敘事錨定（必填）──
description: >
  聖鑰院複合體是普世教會西派教廷的核心聖所，
  由大聖堂、教皇私室、地下墓窖與密道網絡組成。
  其建築風格融合了青銅時代的階梯式神殿與中古時期的哥特尖頂。

# ── 感官錨定（必填，room 與 district 層級強制）──
atmosphere:
  scent:                          # 氣味陣列，可有多種
    - 陳年薰香                    # 原文有直接描述
    - 地下潮濕霉味                # inferred: true（見下方規則）
  light: 彩色玻璃過濾的昏黃夕照   # 光線質地
  temperature: 陰涼               # 溫度感受
  sound:                          # 聲音陣列
    - 遠處鐘聲迴盪
    - 低聲禱告

# ── 屬性標籤（可選但建議填寫）──
properties:
  controlled_by: 普世教會西派教廷  # 控制勢力
  access_level: restricted        # [public|restricted|private|secret]
  danger_level: low               # [none|low|medium|high|deadly]
  religion: 太陽神阿努信仰         # 主要信仰
  population: 0                   # 常駐人口（區域/定居點層級建議填寫）

# ── 關係即通道（connections，可選）──
connections:
  - target: grand_cathedral       # 目標地點 id
    type: physical                # [physical|secret|conceptual|scent|sound]
    direction: north              # 相對方向或描述
    hidden: false                 # 是否為密道
    description: 正門直通的宏偉大聖堂
  - target: papal_tomb
    type: secret
    direction: 地下
    hidden: true
    description: 僅教皇與守鑰人知曉的螺旋階梯

# ── 內容物（contents，可選）──
contents:
  - item: artifact
    name: 聖鑰·旭日之扉
    location: 教皇私室壁龕
    guardian: 守鑰人騎士團
    description: 傳說中能打開艾爾達拉世界樹核心密室的金色鑰匙

# ── 歷史事件（events，可選）──
events:
  - id: iron_crown_uprising
    year: 726
    name: 鐵冠起義
    description: 鐵冠騎士團攻佔聖鑰院，教廷分裂為東西兩派

# ── 快速標籤（tags，必填）──
tags:
  - 宗教
  - 教廷
  - 夕照之地
  - 聖所
  - 密道
```

---

## 三、欄位詳細規範

### `id`
- **型別**：string
- **格式**：snake_case，全局唯一
- **規則**：只允許小寫字母、數字、底線；不可使用連字號或空格
- **範例**：`sacred_key_complex`、`vetustapolis_harbor`、`west_seraphion`

### `layer`
- **型別**：string
- **允許值**：`continent`、`geography`、`empire`、`settlement`、`district`、`room`
- **規則**：不可自創層級名稱

### `parent_id`
- **型別**：string 或 null
- **規則**：
  - `continent` 可為 `null`
  - 其他層級必須指向上一層的真實 `id`
  - `geography` 指向 `continent` 或另一 `geography`
  - `empire` 指向 `continent`
  - `settlement` 指向 `empire` 或 `geography`（如位於山脈中的定居點）
  - `district` 指向 `settlement`
  - `room` 指向 `district`

### `atmosphere`
- **型別**：object
- **必填子欄位**：
  - `scent`：string[]（氣味陣列，至少一項，若無法確定則填 `[]`）
  - `light`：string（光線質地描述）
  - `temperature`：string（溫度感受）
  - `sound`：string[]（聲音陣列，至少一項，若無法確定則填 `[]`）
- **推斷規則**：若某感官細節並非原文明確描述，必須在值後方或註解中標記 `inferred: true`。機器驗證時不強制檢查此標記，但人類審查時必須可見。

### `connections`
- **型別**：object[]
- **必填子欄位**：
  - `target`：string（目標地點 `id`）
  - `type`：string（`physical`、`secret`、`conceptual`、`scent`、`sound`）
  - `direction`：string（相對方向或描述性方位）
- **可選子欄位**：
  - `hidden`：boolean（預設 `false`）
  - `description`：string（通道的敘事描述）
- **交叉引用檢查**：`target` 必須指向 `data/` 下某個 YAML 的真實 `id`

### `contents`
- **型別**：object[]
- **必填子欄位**：
  - `item`：string（`artifact`、`npc`、`document`、`resource`、`landmark`）
  - `name`：string
- **可選子欄位**：
  - `location`：string（在該地點內的具體位置）
  - `guardian`：string（守護者或保管者）
  - `description`：string

### `events`
- **型別**：object[]
- **必填子欄位**：
  - `id`：string（事件唯一識別碼）
  - `year`：integer（安納克曆年份，負數表示洪水前）
  - `name`：string
- **可選子欄位**：
  - `description`：string

### `tags`
- **型別**：string[]
- **規則**：至少一項；建議使用中文標籤，便於搜尋
- **常見標籤**：`宗教`、`軍事`、`商業`、`貴族`、`平民`、`秘境`、`密道`、`戰場`、`神殿`、`宮殿`

---

## 四、檔案命名與目錄規則

1. **檔案名**：必須與 `id` 一致，加 `.yaml` 副檔名。  
   範例：`id: sacred_key_complex` → 檔名 `sacred-key-complex.yaml`

2. **一檔一地點**：每個 YAML 檔案只描述一個地點，不可合併多個地點。

3. **index.yaml 格式**：
   ```yaml
   id: ankora
   name: 安納克大陸
   layer: continent
   description: ...
   empires:
     - id: west_seraphion
       name: 塞拉菲昂神聖帝國
     - id: east_caesaric
       name: 凱撒里克帝國
   ```

---

## 五、定居點粒度分級（Tier System）

粒度分級直接對應 CKII 政治層級（見 AGENTS.md 第三節），而非主觀的「重要性」。這確保架構複雜度只出現在應該出現的地方：

| 級別 | 對應 CKII 層級 | 適用對象 | 目錄結構 | 說明 |
|------|---------------|----------|----------|------|
| **Tier 1** | **Empire Capital** | 帝國首都、聯邦核心 | `locations/{settlement}/` 含 `settlement.yaml` + `district/` + `room/*.yaml` | 維特魯斯、奧斯堡、霍羅托里亞、塔拉薩、席爾瓦裡翁 |
| **Tier 2** | **Duchy / Kingdom Capital** | 選帝侯首都、大公國宮殿、重要自治城邦 | `locations/{settlement}.yaml` 為主，可額外開少數獨立 `room/*.yaml` | 金穗堡、潮音宮、雙子門市、菲惹港等 |
| **Tier 3** | **County（普通）** | 普通城鎮、村莊、哨站、小修道院、邊境堡壘 | 單一 `locations/{settlement}.yaml` | 赤土鎮、小赫斯領、珍珠灣漁村、流泉修道院等 |

### 5.1 為什麼這樣分級？

- **Tier 1 = Empire 心臟**：這些定居點是整個帝國的敘事引擎，內部結構複雜到單一 YAML 無法承載（如維特魯斯的三層空間、奧斯堡的雙頭制同心圓）。
- **Tier 2 = Duchy/Kingdom 心臟**：選帝侯領地首都或重要自治城邦，有自己的政治實體和獨特建築，但未達到帝國首都的敘事密度。例如金穗堡是格蘭迪斯大公國的權力中心，但不需要像維特魯斯那樣拆出 13 個 room。
- **Tier 3 = 普通 County**：CKII 中的基本地塊單位。它們是地圖上的「點」，提供資源、人口、軍事價值，但內部空間不需要獨立展開。

### 5.2 目錄結構範例

**Tier 1（維特魯斯）**：
```
data/01-west-seraphion/locations/vetustapolis/
├── settlement.yaml
├── inner-city/
│   ├── district.yaml
│   └── sacred-key-complex.yaml
└── lower-city/
    ├── district.yaml
    └── bridge-markets.yaml
```

**Tier 2（金穗堡 / 潮音宮）**：
```
data/01-west-seraphion/locations/
├── golden-spire-castle.yaml    # settlement 層，內含 districts/contents
└── golden-spire-rooms/         # 可選：僅關鍵 room 獨立（如大公的戰爭廳）
    └── war-council-hall.yaml
```

**Tier 3（赤土鎮 / 珍珠灣漁村）**：
```
data/01-west-seraphion/locations/red-earth-hamlet.yaml
# 單一檔案，所有 district/room 資訊內嵌於 contents/districts 欄位
```

### 5.3 選擇原則

- **按政治層級判定，而非主觀感受**：新建 settlement 時，先確認它在 CKII 層級中屬於 Empire Capital / Duchy Capital / 普通 County。
- **Tier 2 升級到 Tier 1 需審查**：僅當該定居點有「超過 3 個值得獨立描述的 room 級空間」且敘事密度確實等同帝國首都時，才允許展開為 Tier 1。
- **不強制降級**：已展開的 Tier 1 不會因為「內容變少」而被強制合併回單檔。

### 5.4 欄位使用對照表

| 欄位 | Tier 1 | Tier 2 | Tier 3 |
|------|--------|--------|--------|
| `districts`（預告陣列） | ✅ 必填 | ✅ 建議 | ⚪ 可省略 |
| 獨立 `district.yaml` | ✅ 允許 | ❌ 不允許 | ❌ 不允許 |
| 獨立 `room.yaml` | ✅ 允許 | ✅ 少量（≤5） | ❌ 不允許 |
| `contents`（內嵌 landmark） | ✅ 摘要 | ✅ 主要描述處 | ✅ 主要描述處 |
| `atmosphere`（獨立檔案） | ✅ 每層獨立 | ⚪ 僅 settlement | ⚪ 僅 settlement |

> **核心原則**：`settlement.yaml` 的 `contents` 在 Tier 1 中應保持**摘要性**，詳細描述交給獨立的 `room` 檔案；在 Tier 2/3 中，`contents` 是主要描述載體，允許較長篇幅。

---

## 六、新增地點的標準流程（給協作者）

1. **確認層級**：這個地點是 `empire`、`settlement`、`district` 還是 `room`？
2. **確認粒度級別**：如果是 `settlement`，按 CKII 政治層級判定：
   - Empire Capital → **Tier 1**
   - Duchy / Kingdom Capital → **Tier 2**
   - 普通 County → **Tier 3**（預設）
3. **確認 `parent_id`**：上一層的地點 `id` 是否已存在？若不存在，先建立上層。
4. **複製範本**：
   - Tier 1：從 `vetustapolis/settlement.yaml` 複製結構
   - Tier 2/3：從同帝國內任一單檔 settlement（如 `ostburg.yaml`）複製結構
5. **填寫必填欄位**：`id`、`name`、`layer`、`region`、`empire`、`parent_id`、`description`、`atmosphere`、`tags`。
6. **填寫可選欄位**：`connections`、`contents`、`events` 視原文內容決定。
7. **命名檔案**：`{id}.yaml`（`id` 中的底線改為連字號）。
8. **放入正確目錄**：
   - Tier 1：`data/{帝國前綴}/locations/{定居點}/{區域}/`
   - Tier 2/3：`data/{帝國前綴}/locations/`
9. **跑驗證**：確認 YAML 語法正確，且 `parent_id` 與 `connections[].target` 均可解析。
10. **提交 Git**：一個地點一個 commit，或一批相關地點一個 commit。

---

## 六、常見錯誤

| 錯誤 | 範例 | 修正 |
|------|------|------|
| `id` 含空格或連字號 | `sacred-key` | `sacred_key` |
| `layer` 值不在白名單 | `mountain` | `geography`（請使用標準層級名稱） |
| `parent_id` 指向自己 | `parent_id: sacred_key_complex` | 指向上一層 `inner_city` |
| `connections.target` 不存在 | `target: non_existent_place` | 確認目標 `id` 已建立 |
| `atmosphere.scent` 為 string 而非 array | `scent: 薰香` | `scent: ["薰香"]` |
| 一檔多地點 | 一個 YAML 包含聖鑰院 + 大聖堂 | 拆成兩個檔案 |

---

## 七、版本歷史

| 版本 | 日期 | 變更 |
|------|------|------|
| v0.1 | 2026-05-12 | 初始版本，定義五級層次與基礎欄位 |

---

## 八、勢力層級（Faction Layer）— v0.2 新增

> **狀態**：計劃階段，欄位規範已定，尚未產出具體 YAML。  
> **用途**：描述非國家組織（傭兵團、行會、宗教結社、秘密組織、貿易聯盟）的結構、活動範圍與勢力關係。

### 8.1 設計原則

- **獨立於地點層級**：`faction` 不屬於 `continent → empire → settlement` 鏈，而是與 `geography` 平行的獨立層級
- **活動即影響**：通過 `influence[]` 描述組織在哪些地點有據點、招募點或秘密活動
- **關係網絡**：通過 `relations[]` 描述與其他 `faction` 或 `empire` 的立場（友好/敵對/秘密）
- **感官錨定於總部**：`atmosphere` 描述的是組織總部（`headquarters`）所在的空間感官

### 8.2 Faction YAML 結構（計劃規範）

```yaml
# ── 身份錨定（必填）──
id: frostblade_company
name: 霜刃傭兵團
layer: faction

# ── 組織屬性（必填）──
type: mercenary            # [mercenary|guild|religious|secret_society|trade_league|political|academic]
headquarters: ashtown      # 總部地點 id（可為 settlement 或 room）
founding_year: 780
ideology: 金幣即忠誠，刀劍即法律

# ── 敘事錨定（必填）──
description: >
  北境最著名的傭兵團，由退役霜生戰士與人類混血組成。
  他們在約恩維德山脈南麓的凍土要塞中訓練，
  以能在極寒中戰鬥聞名，收費高昂但從不背叛雇主。

# ── 感官錨定（必填）──
atmosphere:
  scent:
    - 凍土與鐵鏽
    - 傷口藥膏的刺鼻
    - 混合血統士兵的皮革與汗味
  light: 極北長夜的慘白與營火搖曳的橙紅
  temperature: 終年冰寒，室內靠地熱溫泉勉強維持
  sound:
    - 鐵劍互擊的鏗鏘
    - 極北風嘯穿過要塞縫隙
    - 混血士兵的低聲咒罵（夾雜霜生語與人類方言）

# ── 活動範圍（influence，可選但建議填寫）──
influence:
  - target: the_howling_peaks
    presence: outpost
    description: 隘口附近的哨站，監控東西商隊，收取「保護費」
  - target: the_flood_plain
    presence: recruitment
    description: 每年秋季在豐收節市集設攤招募新兵，專挑破產農民
  - target: north_frost
    presence: covert
    description: 團長與某部落首領有血緣關係，暗中獲取霜生戰術情報

# ── 勢力關係（relations，可選但建議填寫）──
relations:
  - target: west_seraphion
    stance: hostile
    description: 曾參與格蘭迪斯大公與皇帝的私戰，殺死過帝國正規軍
  - target: north_frost
    stance: secret
    description: 團長母親是霜生貴族，這個秘密若曝光將摧毀傭兵團的信譽

# ── 關鍵成員（members，可選）──
members:
  - role: 團長
    name: 維爾姆·霜咬
    status: alive
  - role: 創始人
    name: 老約恩
    status: dead

# ── 歷史事件（events，可選）──
events:
  - id: frostblade_founding
    year: 780
    name: 霜刃傭兵團成立
    description: 老約恩率領十七名混血逃兵在凍土要塞立下血誓

# ── 快速標籤（tags，必填）──
tags:
  - 傭兵
  - 北境
  - 混血
  - 極寒作戰
```

### 8.3 欄位規範

#### `type`
- **型別**：string
- **允許值**：`mercenary`、`guild`、`religious`、`secret_society`、`trade_league`、`political`、`academic`
- **說明**：組織的核心性質

#### `headquarters`
- **型別**：string
- **說明**：組織總部所在地的 `id`，通常為 `settlement` 或 `room` 層級

#### `founding_year`
- **型別**：integer
- **說明**：成立年份，安納克曆

#### `ideology`
- **型別**：string
- **說明**：組織的核心理念或口號，簡短有力

#### `influence[]`
- **型別**：object[]
- **說明**：組織在各地點的活動痕跡
- **必填子欄位**：
  - `target`：string（地點 `id`）
  - `presence`：string（`headquarters`、`stronghold`、`outpost`、`recruitment`、`covert`、`ritual_site`）
  - `description`：string

#### `relations[]`
- **型別**：object[]
- **說明**：與其他勢力的關係
- **必填子欄位**：
  - `target`：string（`empire` 或 `faction` 的 `id`）
  - `stance`：string（`allied`、`friendly`、`neutral`、`hostile`、`secret`）
  - `description`：string

#### `members[]`
- **型別**：object[]
- **說明**：關鍵成員清單
- **子欄位**：
  - `role`：string
  - `name`：string
  - `status`：string（`alive`、`dead`、`missing`、`legendary`）

### 8.4 目錄規則

Faction YAML 統一放於 `data/factions/` 目錄，不按帝國分區：

```
data/
├── factions/
│   ├── frostblade-company.yaml
│   ├── silverleaf-consortium.yaml
│   ├── sisters-of-the-tear.yaml
│   └── ash-covenant.yaml
```

> **理由**：faction 跨越多個帝國與地理區域，不適合歸入單一帝國目錄。

---

## 九、版本歷史

| 版本 | 日期 | 變更 |
|------|------|------|
| v0.1 | 2026-05-12 | 初始版本，定義五級層次與基礎欄位 |
| v0.2 | 2026-05-12 | 新增 `faction` 層級計劃，定義非國家組織的欄位規範（`influence`、`relations`、`members`）|
