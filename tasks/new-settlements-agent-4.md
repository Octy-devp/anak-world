# 任務書：Agent 4 — 非選帝侯公爵領（2個新Duchy，6個County）

## 目標
建立 2 個非選帝侯公爵領，每個含 1 個首都（Tier 2）+ 2 個下屬 Tier 3 County。

---

## 公爵領一：東境邊防公國（Duchy of Eastmark）

與凱撒里克帝國接壤的邊境地帶，承擔魯普圖斯隘口以南的防禦壓力。
非選帝侯，但軍事地位重要。首都為邊境要塞。

### 1. 首都：`data/01-west-seraphion/locations/aurora-castra.yaml`
- `id`: `aurora_castra`
- `name`: 奧羅拉堡（拉丁 Aurora Castra = 黎明要塞）
- `layer`: `settlement`
- `settlement_type`: `fortress`
- `region`: 東部邊境
- `empire`: 塞拉菲昂神聖帝國
- `parent_id`: `west_seraphion`
- 定位：東境邊防公國首都，石砌邊境要塞，監控凱撒里克動向

### 2. 下屬：`data/01-west-seraphion/locations/specula-ruptus.yaml`
- `id`: `specula_ruptus`
- `name`: 斯佩庫拉魯普圖斯哨塔（拉丁 Specula Ruptus = 隘口瞭望塔）
- `layer`: `settlement`
- `settlement_type`: `outpost`
- `region`: 東部邊境
- `empire`: 塞拉菲昂神聖帝國
- `parent_id`: `west_seraphion`
- 定位：魯普圖斯隘口附近的監視哨塔，第一時間通報東方動向

### 3. 下屬：`data/01-west-seraphion/locations/via-mercatorum.yaml`
- `id`: `via_mercatorum`
- `name`: 維亞默卡托魯姆商道村（拉丁 Via Mercatorum = 商人之路）
- `layer`: `settlement`
- `settlement_type`: `village`
- `region`: 東部邊境
- `empire`: 塞拉菲昂神聖帝國
- `parent_id`: `west_seraphion`
- 定位：東西商隊必經之路上的小村，客棧、馬廄、補給站

---

## 公爵領二：席爾瓦因邊境領（March of Sylvaine）

與艾爾達拉秘境（世界樹森林）接壤的邊境地帶。
非選帝侯，由教廷任命的邊境修道院長管理，主要任務是監控森民動向。
**重要警告：森民（席爾凡）是完全隔離的，不可設定混居。**

### 4. 首都：`data/01-west-seraphion/locations/radix-specula.yaml`
- `id`: `radix_specula`
- `name`: 拉迪克斯守望修道院（拉丁 Radix Specula = 根之瞭望）
- `layer`: `settlement`
- `settlement_type`: `monastery`（兼邊境哨站功能）
- `region`: 西南邊境
- `empire`: 塞拉菲昂神聖帝國
- `parent_id`: `west_seraphion`
- 定位：席爾瓦因邊境領首都，修道院兼邊境防禦據點，修士同時是哨兵

### 5. 下屬：`data/01-west-seraphion/locations/terminus-hamlet.yaml`
- `id`: `terminus_hamlet`
- `name`: 特爾米努斯邊境村（拉丁 Terminus = 邊界）
- `layer`: `settlement`
- `settlement_type`: `village`
- `region`: 西南邊境
- `empire`: 塞拉菲昂神聖帝國
- `parent_id`: `west_seraphion`
- 定位：帝國與艾爾達拉秘境邊界上的農奴村，村民時常聽到森林深處的奇異聲響，但從未見過森民

### 6. 下屬：`data/01-west-seraphion/locations/arbor-tower.yaml`
- `id`: `arbor_tower`
- `name`: 阿爾博塔瞭望塔（拉丁 Arbor = 樹）
- `layer`: `settlement`
- `settlement_type`: `outpost`
- `region`: 西南邊境
- `empire`: 塞拉菲昂神聖帝國
- `parent_id`: `west_seraphion`
- 定位：建於巨樹殘骸上的瞭望塔，監控世界樹森林邊緣的動向

---

## 規範
- 全部參照 `SCHEMA.md` 第二節與第五節
- Tier 2（首都）：單檔為主，可額外開少數獨立 room（目前不需要）
- Tier 3（下屬）：單一 YAML，無獨立 district/room
- 必填：`id`, `name`, `layer`, `region`, `empire`, `parent_id`, `description`, `atmosphere`, `tags`
- `atmosphere` 必須包含 `scent`, `light`, `temperature`, `sound`

## 已知連接
- `aurora_castra` → `the_howling_peaks`（怒嘯山脈，東界）、`ruptus_pass`（魯普圖斯隘口）
- `specula_ruptus` → `ruptus_pass`
- `via_mercatorum` → `flumen_geminus`（傑米努斯河，商道沿河流）
- `radix_specula` → `eldara_worldtree`（艾爾達拉世界樹，conceptual 連接，強調隔離與監視）
- `terminus_hamlet` → `eldara_worldtree`（邊界鄰接）
- `arbor_tower` → `eldara_worldtree`

## 命名風格
- 東境邊防公國：拉丁文（Aurora Castra, Specula Ruptus, Via Mercatorum）
- 席爾瓦因邊境領：拉丁文（Radix Specula, Terminus, Arbor Tower）

## 注意事項
- 全部標註 `inferred: true`（這些是推斷產生的政治實體與定居點）
- **森民隔離警告**：席爾瓦因邊境領的描述中，森民必須保持神秘與隔離。人類村民可以「感受到森林的異樣」或「發現奇怪痕跡」，但絕對不能與森民混居、交易或對話。
- 東境邊防公國特徵：凱撒里克壓力、軍事化、商隊往來
- 席爾瓦因邊境領特徵：教廷監控、森林恐懼、森民隔離、邊境緊張
