# 路由與頁面設計文件 (ROUTES)

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| --- | --- | --- | --- | --- |
| 首頁 | GET | `/` | `index.html` | 顯示近期活動列表，並提供建立新活動的表單 |
| 建立活動 | POST | `/activities` | — | 接收新活動名稱，存入 DB，完成後重導向至活動管理頁 |
| 活動管理頁 | GET | `/activities/<int:activity_id>` | `activities/detail.html` | 顯示候選名單、抽獎結果，並包含「新增名單表單」與「選擇抽出人數與抽籤」 |
| 新增名單 | POST | `/activities/<int:activity_id>/candidates` | — | 接收使用者輸入的多行名單，存入 DB，重導向回活動管理頁 |
| 執行抽籤 | POST | `/activities/<int:activity_id>/draw` | `activities/draw_result.html` | 接收要抽出的人數參數，隨機選取未抽出的名單並更新 DB 狀態，渲染或重導向至結果展示頁 |
| 重置名單 | POST | `/activities/<int:activity_id>/reset` | — | 將此活動下所有名單的 `is_drawn` 狀態設為 0，重導向回活動管理頁 |
| 刪除活動 | POST | `/activities/<int:activity_id>/delete` | — | 刪除此活動與其所有名單，完成後重導向回首頁 |

## 2. 每個路由的詳細說明

### `GET /`
- **處理邏輯**：呼叫 `Activity.get_all()` 取得目前所有的抽籤活動。
- **輸出**：渲染 `index.html`，並將活動列表傳入給模板。
- **錯誤處理**：無。

### `POST /activities`
- **輸入**：表單欄位 `name` (活動名稱)。
- **處理邏輯**：驗證 `name` 不為空後，呼叫 `Activity.create(name)`。
- **輸出**：重導向至 `/activities/<新產生的 id>`。
- **錯誤處理**：若名稱空白，可透過 Flash message 提示，重導向回 `/`。

### `GET /activities/<int:activity_id>`
- **輸入**：URL 參數 `activity_id`。
- **處理邏輯**：
  1. 呼叫 `Activity.get_by_id(activity_id)`。
  2. 呼叫 `Candidate.get_undrawn_by_activity(activity_id)` 取得未抽出名單。
  3. 呼叫 `Candidate.get_drawn_by_activity(activity_id)` 取得已抽出名單。
- **輸出**：渲染 `activities/detail.html`。
- **錯誤處理**：若活動不存在，回傳 404 Not Found。

### `POST /activities/<int:activity_id>/candidates`
- **輸入**：表單欄位 `candidate_names` (多行字串 textarea)。
- **處理邏輯**：以換行符號切割字串、去除空白後，呼叫 `Candidate.create_many()` 批次建檔。
- **輸出**：重導向回 `/activities/<activity_id>`。
- **錯誤處理**：若沒有輸入任何有效文字，重導向回去並給予提示。

### `POST /activities/<int:activity_id>/draw`
- **輸入**：表單欄位 `draw_count` (預計抽出人數，預設為 1)。
- **處理邏輯**：
  1. 透過 `Candidate.get_undrawn_by_activity()` 取得未抽出清單。
  2. 此處應在 Python 程式碼隨機打亂名單（`random.sample()`）取出相對應人數。
  3. 將抽中者的 ID 透過 `Candidate.mark_as_drawn()` 標記為已中獎。
- **輸出**：將中獎者名單與活動資訊傳遞到 `activities/draw_result.html` 給予動畫/清晰展示，畫面應包含按鈕可返回管理頁。
- **錯誤處理**：若未抽出清單人數少於 `draw_count`，則全部抽出並給予提示。

### `POST /activities/<int:activity_id>/reset`
- **輸入**：無。
- **處理邏輯**：呼叫 `Candidate.reset_drawn_status()`。
- **輸出**：重導向回 `/activities/<activity_id>`。

### `POST /activities/<int:activity_id>/delete`
- **輸入**：無。
- **處理邏輯**：呼叫 `Activity.delete()`。
- **輸出**：重導向回 `/`。

---

## 3. Jinja2 模板清單

所有的模板檔案會建立在 `app/templates/` 中。

1. **`base.html`**
   - 所有頁面的根模板
   - 包含共通的 CSS 引用、標頭（Header）與頁尾（Footer）、Flash Message 顯示區域。

2. **`index.html`**
   - 繼承自 `base.html`
   - 功能：展示活動清單以及建立活動視窗。

3. **`activities/detail.html`**
   - 繼承自 `base.html`
   - 功能：活動詳情面板。左側或上方可貼上名單增加候補項目，右側或下方列出「抽出按鈕」、未中籤名單、已中籤名單。

4. **`activities/draw_result.html`**
   - 繼承自 `base.html`
   - 功能：顯示抽出的驚喜結果，包含 CSS 放大/特效，確認結果後「返回活動列表」按鈕。

---

## 4. 路由骨架程式碼
請參考 `app/routes/` 內的 `.py` 檔案。
