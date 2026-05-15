# 子代理任務書：geo-connection-audit

## 目標
審計所有 `data/*/geographies/*.yaml` 的 connections 雙向一致性，並檢查 `index.yaml` 的完整性。

## 輸出
不寫入新檔案。將審計報告寫入本任務書末尾的「審計報告」區塊。

## 審計範圍
所有位於以下目錄的 `*.yaml` 檔案：
- `data/01-west-seraphion/geographies/*.yaml`
- `data/02-east-caesaric/geographies/*.yaml`
- `data/03-north-frost/geographies/*.yaml`
- `data/04-south-libertania/geographies/*.yaml`
- `data/05-secret-eldara/geographies/*.yaml`

## 審計項目

### 1. 雙向連接一致性（Bidirectional Connection Consistency）
對於每一個 geography YAML 中的每一個 connection：
- 檢查 `target` 所指向的 YAML 檔案是否存在於 `data/` 下
- 檢查目標 YAML 是否有對稱的 connection 指回來（target = 原檔案的 id）
- 檢查對稱 connection 的 `type` 是否一致（或至少相容）
- 記錄所有不一致、缺失對稱連接、或目標不存在的問題

### 2. index.yaml 完整性
- 檢查 `data/index.yaml` 的 `geographies:` 列表中是否包含了所有在 `data/*/geographies/*.yaml` 中定義的 geography id
- 檢查是否有 index.yaml 中列出但實際檔案不存在的 geography id
- 記錄所有缺失或多餘的項目

### 3. 跨帝國連接合理性
- 檢查跨帝國的 physical 連接是否合理（例如：兩個相隔遙遠的地理實體標記為 physical 連接）
- 檢查 connections 中的 direction 描述是否與兩個實體的相對位置一致（可參考 map.txt 或地理位置推斷）

## 權威性優先級
- `data/*/geographies/*.yaml` 為最高權威
- `data/index.yaml` 次之
- `map.txt` 僅供參考，若與 YAML 衝突，以 YAML 為準

## 禁止事項
- **不得修改任何 YAML 檔案**（這是審計子代理，只讀不寫）
- 不得修改 SCHEMA.md 或 schema.json
- 不得創建新檔案或目錄

## 上下文恢復
啟動時請依次讀取：
1. `/workspaces/anak-world/PLAN.md`
2. `/workspaces/anak-world/SCHEMA.md`
3. `/workspaces/anak-world/TASKLOG.md`
4. `/workspaces/anak-world/data/index.yaml`
5. 掃描所有 `data/*/geographies/*.yaml`

## 審計報告格式

```markdown
## 審計報告

### 雙向連接一致性
| 檔案 | connection target | 問題類型 | 嚴重程度 | 建議修正 |
|------|------------------|---------|---------|---------|
| ... | ... | 缺失對稱連接 / 目標不存在 / type 不一致 | high/medium/low | ... |

### index.yaml 完整性
| id | 存在於 index? | 存在於檔案? | 問題 |
|----|--------------|------------|------|
| ... | ... | ... | ... |

### 跨帝國連接合理性
| 檔案A | 檔案B | type | 問題 |
|-------|-------|------|------|
| ... | ... | ... | ... |
```

## 完成標準
- [ ] 所有 geography YAML 的 connections 已審查
- [ ] index.yaml 的 geographies 列表已核對
- [ ] 審計報告已寫入本任務書末尾

---

## 審計報告

> **審計時間**：2026-05-15  
> **審計範圍**：`data/*/geographies/*.yaml`（共 19 個檔案）  
> **審計工具**：子代理 `geo-connection-audit`（只讀）

---

### 統計摘要

| 類別 | 數量 | 備註 |
|------|------|------|
| **雙向 type 不一致** | **2** | high |
| **缺失對稱連接（physical）** | **17** | medium |
| **缺失對稱連接（conceptual）** | **9** | low |
| **目標不存在** | **0** | 所有 target 均可解析 |
| **index.yaml 缺失** | **7** | medium |
| **index.yaml 冗餘** | **0** | 所有 index 條目均有對應檔案 |

---

### 雙向連接一致性

| 檔案 | connection target | 問題類型 | 嚴重程度 | 建議修正 |
|------|------------------|---------|---------|---------|
| `flumen-geminus.yaml` | `northern_mountains` | type 不一致（physical vs conceptual） | **high** | `northern_mountains` 應改為 physical，與河流實體交匯相符 |
| `the-howling-peaks.yaml` | `jarnvid_river` | type 不一致（physical vs conceptual） | **high** | `jarnvid_river` 應改為 physical，河流發源於山脈北麓為實體關係 |
| `lacus-speculum.yaml` | `the_howling_peaks` | 缺失對稱連接 | medium | `the-howling-peaks.yaml` 應追加指向 `lacus_speculum` 的 connection |
| `lacus-speculum.yaml` | `northern_mountains` | 缺失對稱連接 | medium | `northern-mountains.yaml` 應追加指向 `lacus_speculum` 的 connection |
| `lacus-speculum.yaml` | `flumen_geminus` | 缺失對稱連接 | medium | `flumen-geminus.yaml` 應追加指向 `lacus_speculum` 的 connection |
| `lacus-speculum.yaml` | `jarnvid_river` | 缺失對稱連接 | medium | `jarnvid-river.yaml` 應追加指向 `lacus_speculum` 的 connection |
| `palus-nebulae.yaml` | `the_flood_plain` | 缺失對稱連接 | medium | `the-flood-plain.yaml` 應追加指向 `palus_nebulae` 的 connection |
| `palus-nebulae.yaml` | `flumen_geminus` | 缺失對稱連接 | medium | `flumen-geminus.yaml` 應追加指向 `palus_nebulae` 的 connection |
| `palus-nebulae.yaml` | `the_howling_peaks` | 缺失對稱連接 | medium | `the-howling-peaks.yaml` 應追加指向 `palus_nebulae` 的 connection |
| `delta-aurum.yaml` | `aurum_river` | 缺失對稱連接 | medium | `aurum-river.yaml` 應追加指向 `delta_aurum` 的 connection |
| `campus-cinereus.yaml` | `aurum_river` | 缺失對稱連接 | medium | `aurum-river.yaml` 應追加指向 `campus_cinereus` 的 connection |
| `septempontis-vallis.yaml` | `the_howling_peaks` | 缺失對稱連接 | medium | `the-howling-peaks.yaml` 應追加指向 `septempontis_vallis` 的 connection |
| `northern-mountains.yaml` | `the_howling_peaks` | 缺失對稱連接 | medium | `the-howling-peaks.yaml` 應追加指向 `northern_mountains` 的 connection |
| `sylvaine-river.yaml` | `eldara_worldtree` | 缺失對稱連接 | medium | `eldara-worldtree.yaml` 應追加指向 `sylvaine_river` 的 connection |
| `silva-argentea.yaml` | `eldara_worldtree` | 缺失對稱連接 | medium | `eldara-worldtree.yaml` 應追加指向 `silva_argentea` 的 connection |
| `silva-argentea.yaml` | `sylvaine_river` | 缺失對稱連接 | medium | `sylvaine-river.yaml` 應追加指向 `silva_argentea` 的 connection |
| `silva-argentea.yaml` | `southern_mountains` | 缺失對稱連接 | medium | `southern-mountains.yaml` 應追加指向 `silva_argentea` 的 connection |
| `flumen-geminus.yaml` | `wind_isles` | 缺失對稱連接（conceptual） | low | `wind-isles.yaml` 可選追加指向 `flumen_geminus` 的 conceptual 連接 |
| `the-flood-plain.yaml` | `the_howling_peaks` | 缺失對稱連接（conceptual） | low | `the-howling-peaks.yaml` 可選追加 |
| `the-flood-plain.yaml` | `eldara_worldtree` | 缺失對稱連接（conceptual） | low | `eldara-worldtree.yaml` 可選追加 |
| `aurum-river.yaml` | `the_howling_peaks` | 缺失對稱連接（conceptual） | low | `the-howling-peaks.yaml` 可選追加 |
| `wind-isles.yaml` | `the_abyssus` | 缺失對稱連接（conceptual） | low | `the-abyssus.yaml` 可選追加 |
| `wind-isles.yaml` | `eldara_worldtree` | 缺失對稱連接（conceptual） | low | `eldara-worldtree.yaml` 可選追加 |
| `wind-isles.yaml` | `the_howling_peaks` | 缺失對稱連接（conceptual） | low | `the-howling-peaks.yaml` 可選追加 |
| `southern-mountains.yaml` | `wind_isles` | 缺失對稱連接（conceptual） | low | `wind-isles.yaml` 可選追加 |
| `tartarus-stream.yaml` | `eldara_worldtree` | 缺失對稱連接（conceptual） | low | `eldara-worldtree.yaml` 可選追加 |

> **說明**：所有 connection target（含指向 empire、settlement 的 target）均可解析為 `data/` 下的真實 YAML 檔案，無「目標不存在」問題。

---

### index.yaml 完整性

| id | 存在於 index? | 存在於檔案? | 問題 |
|----|--------------|------------|------|
| `the_howling_peaks` | ✅ | ✅ | 無 |
| `northern_mountains` | ✅ | ✅ | 無 |
| `southern_mountains` | ✅ | ✅ | 無 |
| `ruptus_pass` | ✅ | ✅ | 無 |
| `flumen_geminus` | ✅ | ✅ | 無 |
| `aurum_river` | ✅ | ✅ | 無 |
| `jarnvid_river` | ✅ | ✅ | 無 |
| `tartarus_stream` | ✅ | ✅ | 無 |
| `the_flood_plain` | ✅ | ✅ | 無 |
| `eldara_worldtree` | ✅ | ✅ | 無 |
| `the_abyssus` | ✅ | ✅ | 無 |
| `wind_isles` | ✅ | ✅ | 無 |
| `lacus_speculum` | ❌ | ✅ | **index 缺失** |
| `palus_nebulae` | ❌ | ✅ | **index 缺失** |
| `silva_argentea` | ❌ | ✅ | **index 缺失** |
| `campus_cinereus` | ❌ | ✅ | **index 缺失** |
| `delta_aurum` | ❌ | ✅ | **index 缺失** |
| `septempontis_vallis` | ❌ | ✅ | **index 缺失** |
| `sylvaine_river` | ❌ | ✅ | **index 缺失** |

> **index.yaml 冗餘檢查**：index 中列出的 12 個 geography id 均有對應 YAML 檔案，無幽靈條目。

---

### 跨帝國連接合理性

| 檔案A | 檔案B | type | 評估 |
|-------|-------|------|------|
| `the-howling-peaks.yaml` | `campus-cinereus.yaml` | physical | ✅ 合理——怒嘯山脈東麓地質延伸至凱撒里克境內的灰燼荒地 |
| `aurum-river.yaml` | `wind-isles.yaml` | physical | ✅ 合理——奧魯姆河出海口外海即風息群島，自然水文連接 |
| `delta-aurum.yaml` | `wind-isles.yaml` | physical | ✅ 合理——三角洲與群島為海陸交界，商船航線自然通道 |
| `ruptus-pass.yaml` | `west_seraphion` | physical | ⚠️ 注意——指向 empire 層級的 physical 連接，schema 允許但建議確認是否應改為 conceptual 或改指向 `the_flood_plain` |
| `ruptus-pass.yaml` | `east_caesaric` | physical | ⚠️ 注意——同上，指向 empire 層級的 physical 連接 |

**總體評估**：跨帝國 physical 連接均為自然地理實體（山脈、河流、海岸線）之間的相鄰關係，無明顯空間矛盾。唯一值得商榷的是 `ruptus_pass` 以 physical 類型直接指向兩個 empire，雖然 schema 允許跨層級連接，但隘口作為 geography 實體，其 physical 鄰接的應是同層級的地理單元（如沖積平原、東部平原），而非政治實體本身。

---

### 最重要的 5 個問題

1. **Type 不一致 x2（high）**：`flumen_geminus ↔ northern_mountains` 與 `the_howling_peaks ↔ jarnvid_river` 的連接類型在雙向檔案中不一致（physical vs conceptual）。河流與山脈的發源/匯入關係屬於實體空間關係，應統一為 physical。

2. **index.yaml 缺失 7 個 geography 條目（medium）**：第二批新增的地理實體（鏡湖、迷霧沼澤、銀葉林、灰燼荒地、黃金三角洲、七橋峽谷、希爾薇恩河）未納入 `data/index.yaml` 的 `geographies:` 列表，導致大陸索引不完整。

3. **`the_howling_peaks.yaml` 是最主要的對稱連接收點（medium）**：該檔案被 7 個其他 geography 檔案指向（`lacus_speculum`、`palus_nebulae`、`aurum_river`、`septempontis_vallis`、`northern_mountains`、`the_flood_plain`、`wind_isles`），但僅有 3 個對稱回連（`flumen_geminus`、`jarnvid_river`、`ruptus_pass`）。作為中央山脈核心，應補齊與周邊地理實體的對稱連接。

4. **`eldara_worldtree.yaml` 缺失 4 個對稱回連（medium）**：被 `silva_argentea`、`sylvaine_river`、`tartarus_stream`、`the_flood_plain`、`wind_isles` 共 5 個檔案指向，但僅回連 `the_howling_peaks` 與 `flumen_geminus`。世界樹作為西南部核心，與銀葉林、希爾薇恩河的連接應為 physical 對稱。

5. **新增 geography 檔案的連接網絡孤立（medium）**：`lacus_speculum`、`palus_nebulae`、`silva_argentea`、`campus_cinereus`、`delta_aurum`、`septempontis_vallis` 均有多個外向連接，但接收端幾乎無一回連，顯示第二批 geography 的連接閉合尚未完成。

---

### 完成標準

- [x] 所有 geography YAML 的 connections 已審查（19 / 19）
- [x] index.yaml 的 geographies 列表已核對
- [x] 審計報告已寫入本任務書末尾

---

## 最終審計報告（Batch A 修復後）

> **審計時間**：2026-05-15（最終）
> **審計範圍**：`data/*/geographies/*.yaml`（共 19 個檔案）
> **審計工具**：子代理 `geo-connection-audit`（只讀）

---

### 統計摘要

| 類別 | 第一次審計 | 最終審計 | 改善 |
|------|-----------|---------|------|
| **雙向 type 不一致** | **2** | **0** | ✅ 全部修復 |
| **缺失對稱連接（physical）** | **17** | **2** | ✅ 大幅改善（剩 2） |
| **缺失對稱連接（conceptual）** | **9** | **3** | ✅ 大幅改善（剩 3） |
| **目標不存在** | **0** | **0** | ✅ 無變化（所有 target 可解析） |
| **index.yaml 缺失** | **7** | **0** | ✅ 全部修復 |
| **index.yaml 冗餘** | **0** | **0** | ✅ 無變化 |

---

### 雙向連接一致性（剩餘問題）

| 檔案 | connection target | 問題類型 | 嚴重程度 | 建議修正 |
|------|------------------|---------|---------|---------|
| `campus-cinereus.yaml` | `aurum_river` | 缺失對稱連接（physical） | medium | `aurum-river.yaml` 應追加指向 `campus_cinereus` 的 physical 連接 |
| `delta-aurum.yaml` | `aurum_river` | 缺失對稱連接（physical） | medium | `aurum-river.yaml` 應追加指向 `delta_aurum` 的 physical 連接 |
| `flumen-geminus.yaml` | `wind_isles` | 缺失對稱連接（conceptual） | low | `wind-isles.yaml` 可選追加指向 `flumen_geminus` 的 conceptual 連接 |
| `wind-isles.yaml` | `the_abyssus` | 缺失對稱連接（conceptual） | low | `the-abyssus.yaml` 可選追加指向 `wind_isles` 的 conceptual 連接 |
| `southern-mountains.yaml` | `wind_isles` | 缺失對稱連接（conceptual） | low | `wind-isles.yaml` 可選追加指向 `southern_mountains` 的 conceptual 連接 |

> **說明**：
> - 所有 connection target 均可解析為 `data/` 下的真實 YAML 檔案（含 geography 與 settlement 層級），無「目標不存在」問題。
> - `palus-nebulae.yaml` → `molinaria`、`ruina_damni` 與 `silva-argentea.yaml` → `radix_specula` 的 target 均存在於 `locations/` 目錄，屬合法跨層級連接。
> - 第一次審計的 **2 個 type 不一致**（`flumen_geminus ↔ northern_mountains`、`the_howling_peaks ↔ jarnvid_river`）已修復，雙向均統一為 `physical`。
> - 第一次審計的 **17 個 physical 缺失對稱連接** 中，15 個已補齊，剩餘 2 個（`campus_cinereus ↔ aurum_river`、`delta_aurum ↔ aurum_river`）待修復。
> - 第一次審計的 **9 個 conceptual 缺失對稱連接** 中，6 個已補齊或目標已建立回連，剩餘 3 個待修復。

---

### index.yaml 完整性

| id | 存在於 index? | 存在於檔案? | 問題 |
|----|--------------|------------|------|
| 全部 19 個 geography ID | ✅ | ✅ | **無問題** |

> **改善**：第一次審計中缺失的 7 個 geography 條目（`lacus_speculum`、`palus_nebulae`、`silva_argentea`、`campus_cinereus`、`delta_aurum`、`septempontis_vallis`、`sylvaine_river`）已全部納入 `data/index.yaml`。

---

### 跨帝國連接合理性

| 檔案A | 檔案B | type | 評估 |
|-------|-------|------|------|
| `lacus-speculum.yaml` | `northern-mountains.yaml` | physical | ✅ 合理——鏡湖坐落於約恩維德山脈南端，北境與塞拉菲昂邊界地帶 |
| `aurum-river.yaml` | `wind-isles.yaml` | physical | ✅ 合理——奧魯姆河出海口外海即風息群島，自然水文連接 |
| `delta-aurum.yaml` | `wind-isles.yaml` | physical | ✅ 合理——三角洲與群島為海陸交界，商船航線自然通道 |
| `ruptus-pass.yaml` | `west_seraphion` | physical | ⚠️ 注意——指向 empire 層級的 physical 連接，schema 允許但建議確認 |
| `ruptus-pass.yaml` | `east_caesaric` | physical | ⚠️ 注意——同上，指向 empire 層級的 physical 連接 |

**總體評估**：跨帝國 physical 連接均為自然地理實體（山脈、河流、海岸線）之間的相鄰關係，無明顯空間矛盾。`ruptus_pass` 以 physical 類型直接指向兩個 empire 的議題與第一次審計一致，屬設計選擇而非錯誤。

---

### 剩餘最重要的問題

1. **`aurum_river.yaml` 缺失 2 個 physical 對稱回連（medium）**：`campus_cinereus` 與 `delta_aurum` 均指向 `aurum_river`，但 `aurum_river.yaml` 未回連。奧魯姆河與灰燼荒地、河口三角洲為實體空間關係，應補齊。

2. **`wind-isles.yaml` 缺失 3 個 conceptual 對稱回連（low）**：`flumen_geminus`（東方入海口）、`the_abyssus`（西方遠海）、`southern_mountains`（東南方）均指向 `wind_isles`，但 `wind-isles.yaml` 未回連。這些為 conceptual 關係，優先級較低。

---

### 完成標準

- [x] 所有 geography YAML 的 connections 已審查（19 / 19）
- [x] index.yaml 的 geographies 列表已核對
- [x] 最終審計報告已寫入本任務書末尾
