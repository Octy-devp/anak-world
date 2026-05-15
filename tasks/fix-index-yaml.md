# 子代理任務書：fix-index-yaml

## 目標
更新 `data/index.yaml` 的 `geographies:` 列表，補齊所有缺失的 geography 條目。

## 輸出檔案
`/workspaces/anak-world/data/index.yaml`

## 缺失條目（7 個）
以下 geography id 已存在於 `data/*/geographies/*.yaml`，但未列入 `index.yaml`：

| id | 名稱 | 所屬目錄 |
|----|------|---------|
| `lacus_speculum` | 鏡湖 | `data/01-west-seraphion/geographies/lacus-speculum.yaml` |
| `palus_nebulae` | 迷霧沼澤 | `data/01-west-seraphion/geographies/palus-nebulae.yaml` |
| `silva_argentea` | 銀葉森林 | `data/01-west-seraphion/geographies/silva-argentea.yaml` |
| `sylvaine_river` | 希爾薇恩河 | 待確認實際檔案位置 |
| `campus_cinereus` | 東部灰燼荒地 | `data/02-east-caesaric/geographies/campus-cinereus.yaml` |
| `delta_aurum` | 奧魯姆河口三角洲 | `data/02-east-caesaric/geographies/delta-aurum.yaml` |
| `septempontis_vallis` | 七橋峽谷 | `data/02-east-caesaric/geographies/septempontis-vallis.yaml` |

## 執行步驟
1. 讀取現有 `data/index.yaml`
2. 掃描 `data/*/geographies/*.yaml` 確認所有 geography id
3. 將缺失的 7 個條目添加到 `geographies:` 列表末尾
4. 每個條目格式參照現有：
   ```yaml
   - id: xxx
     name: XXX
     region: XX部
     description: >
       簡短描述...
   ```
5. 保持 `description` 簡潔（不超過 2 行），直接引用對應 YAML 的 description 前兩句

## 禁止事項
- 不得刪除或修改 index.yaml 中已有的條目
- 不得修改 schema

## 完成標準
- [ ] index.yaml 包含所有 `data/*/geographies/*.yaml` 中定義的 geography id
- [ ] YAML 語法正確
- [ ] 無幽靈條目（index 中列出但實際檔案不存在的 id）
