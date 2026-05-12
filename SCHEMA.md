# Ankora-World YAML Schema 規範

> **版本**：v0.1  
> **用途**：定義 `data/` 下所有地點 YAML 檔案的欄位、型別與填充規則。  
> **原則**：靜態優先、層次錨定、感官即索引、關係即通道。

---

## 一、五級層次（The Five Tiers）

每個地點必須明確屬於以下五級之一，不可跳級：

| 層級 | 英文名 | 說明 | 範例 |
|------|--------|------|------|
| 大陸 | `continent` | 整個安納克大陸 | Ankora |
| 帝國 | `empire` | 政治實體、國家、帝國 | Seraphion Empire |
| 城市 | `city` | 城市、首都、要塞都市 | Vetustapolis |
| 區域 | `district` | 城市內的行政或功能區塊 | Inner City, Harbor District |
| 房間 | `room` | 可進入的具體空間，最小單位 | Sacred Key Complex, Throne Hall |

> **規則**：`room` 必須有 `parent_id` 指向所屬 `district`；`district` 指向 `city`；依此類推。

---

## 二、單一地點 YAML 結構

```yaml
# ── 身份錨定（必填）──
id: sacred_key_complex           # 全局唯一識別碼，snake_case，不可變
name: 聖鑰院複合體               # 人類可讀名稱
layer: room                      # [continent|empire|city|district|room]
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
  population: 0                   # 常駐人口（區域/城市層級建議填寫）

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
  - 西殿
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
- **允許值**：`continent`、`empire`、`city`、`district`、`room`
- **規則**：不可自創層級名稱

### `parent_id`
- **型別**：string 或 null
- **規則**：
  - `continent` 可為 `null`
  - 其他層級必須指向上一層的真實 `id`
  - `empire` 指向 `continent`
  - `city` 指向 `empire`
  - `district` 指向 `city`
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

2. **目錄結構**：
   ```
   data/
   ├── index.yaml                    # 大陸索引
   ├── 01-west-seraphion/            # 帝國目錄（前綴數字確保排序）
   │   ├── empire.yaml               # 帝國本體資料
   │   └── locations/
   │       └── vetustapolis/         # 城市目錄
   │           ├── city.yaml         # 城市本體資料
   │           └── inner-city/       # 區域名稱用連字號
   │               └── sacred-key-complex.yaml
   ```

3. **一檔一地點**：每個 YAML 檔案只描述一個地點，不可合併多個地點。

4. **index.yaml 格式**：
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

## 五、新增地點的標準流程（給協作者）

1. **確認層級**：這個地點是 `empire`、`city`、`district` 還是 `room`？
2. **確認 `parent_id`**：上一層的地點 `id` 是否已存在？若不存在，先建立上層。
3. **複製範本**：從 `sacred-key-complex.yaml` 複製結構。
4. **填寫必填欄位**：`id`、`name`、`layer`、`region`、`empire`、`parent_id`、`description`、`atmosphere`、`tags`。
5. **填寫可選欄位**：`connections`、`contents`、`events` 視原文內容決定。
6. **命名檔案**：`{id}.yaml`（`id` 中的底線改為連字號）。
7. **放入正確目錄**：`data/{帝國前綴}/locations/{城市}/{區域}/`
8. **跑驗證**：確認 YAML 語法正確，且 `parent_id` 與 `connections[].target` 均可解析。
9. **提交 Git**：一個地點一個 commit，或一批相關地點一個 commit。

---

## 六、常見錯誤

| 錯誤 | 範例 | 修正 |
|------|------|------|
| `id` 含空格或連字號 | `sacred-key` | `sacred_key` |
| `layer` 拼錯 | `Room` | `room`（全小寫） |
| `parent_id` 指向自己 | `parent_id: sacred_key_complex` | 指向上一層 `inner_city` |
| `connections.target` 不存在 | `target: non_existent_place` | 確認目標 `id` 已建立 |
| `atmosphere.scent` 為 string 而非 array | `scent: 薰香` | `scent: ["薰香"]` |
| 一檔多地點 | 一個 YAML 包含聖鑰院 + 大聖堂 | 拆成兩個檔案 |

---

## 七、版本歷史

| 版本 | 日期 | 變更 |
|------|------|------|
| v0.1 | 2026-05-12 | 初始版本，定義五級層次與基礎欄位 |
