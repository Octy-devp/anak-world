# 子代理任務書：fix-type-and-major-symmetric

## 目標
修正 2 對 type 不一致的 connection，並為 `the_howling_peaks` 補全缺失的對稱連接。

## 需要修正的檔案
1. `data/01-west-seraphion/geographies/flumen-geminus.yaml`
2. `data/01-west-seraphion/geographies/the-howling-peaks.yaml`
3. `data/03-north-frost/geographies/jarnvid-river.yaml`（或 northern-mountains.yaml，視實際檔案位置而定）

## 任務 1：Type 不一致修正

### 1a. `flumen_geminus` ↔ `northern_mountains`
- 讀取 `flumen-geminus.yaml` 和 `northern-mountains.yaml`
- 檢查雙方的 connection type
- 統一為 `physical`（河流與山脈的發源關係是實體空間關係）
- 使用 `StrReplaceFile` 修改需要調整的一方

### 1b. `the_howling_peaks` ↔ `jarnvid_river`
- 讀取 `the-howling-peaks.yaml` 和 `jarnvid-river.yaml`
- 檢查雙方的 connection type
- 統一為 `physical`（河流發源於山脈北麓是實體空間關係）
- 使用 `StrReplaceFile` 修改需要調整的一方

## 任務 2：為 `the_howling_peaks` 補全對稱連接

`the_howling_peaks` 被以下 geography 指向，但缺少對稱回連：
- `lacus_speculum`（physical）
- `palus_nebulae`（physical）
- `the_flood_plain`（physical/conceptual）
- `aurum_river`（conceptual）
- `septempontis_vallis`（physical）
- `northern_mountains`（physical，同時修正 type）
- `sylvaine_river`（physical）
- `wind_isles`（conceptual）
- `southern_mountains`（physical）

### 執行步驟
1. 讀取 `the-howling-peaks.yaml`
2. 讀取上述每個目標 YAML，確認其連接的 direction 和 description
3. 在 `the-howling-peaks.yaml` 的 `connections:` 區塊末尾，為每個缺失的目標添加對稱連接
4. 對稱連接的 `type` 應與對方一致，`direction` 應為對方 direction 的反向描述

## 禁止事項
- 不得修改 SCHEMA.md 或 schema.json
- 不得刪除任何既有連接

## 完成標準
- [ ] 2 對 type 不一致已修正
- [ ] `the_howling_peaks` 已回連所有指向它的 geography
- [ ] 所有修改後的 YAML 語法正確
