# 子代理任務書：fix-eldara-and-batch2-symmetric

## 目標
為 `eldara_worldtree` 和第二批 geography（`lacus_speculum`、`palus_nebulae`、`silva_argentea`）補全對稱連接。

## 需要修正的檔案
1. `data/05-secret-eldara/geographies/eldara-worldtree.yaml`
2. `data/01-west-seraphion/geographies/lacus-speculum.yaml`
3. `data/01-west-seraphion/geographies/palus-nebulae.yaml`
4. `data/01-west-seraphion/geographies/silva-argentea.yaml`

## 任務 1：`eldara_worldtree` 對稱連接

`eldara_worldtree` 被以下 geography 指向，但僅回連 `the_howling_peaks` 與 `flumen_geminus`：
- `silva_argentea`（physical）
- `sylvaine_river`（physical）
- `tartarus_stream`（physical/conceptual）
- `the_flood_plain`（conceptual）
- `wind_isles`（conceptual）

執行步驟：
1. 讀取 `eldara-worldtree.yaml`
2. 讀取上述每個目標 YAML，確認其連接內容
3. 在 `eldara-worldtree.yaml` 添加對稱回連

## 任務 2：第二批 geography 的對稱連接

`lacus_speculum`、`palus_nebulae`、`silva_argentea` 均有 3-4 個外向連接，但接收端無一回連。

執行步驟：
1. 讀取這三個 YAML
2. 對每個檔案，檢查其 `connections:` 中每個 target
3. 讀取每個 target YAML，確認是否已有對稱回連
4. 若缺失，在 target YAML 中添加對稱回連（而非修改這三個檔案本身）

### 預計需要修改的目標檔案
- `the_howling_peaks.yaml`（可能已由其他子代理修改，檢查後補齊剩餘）
- `flumen_geminus.yaml`
- `northern_mountains.yaml`
- `jarnvid_river.yaml`
- `the_flood_plain.yaml`
- `ruina_damni.yaml`（若 palus_nebulae 指向它）

## 禁止事項
- 不得修改 SCHEMA.md 或 schema.json
- 不得刪除任何既有連接

## 完成標準
- [ ] `eldara_worldtree` 已回連所有指向它的 geography
- [ ] 第二批 geography 的所有外向連接均有對稱回連
- [ ] 所有修改後的 YAML 語法正確
