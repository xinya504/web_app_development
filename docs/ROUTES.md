# 路由與頁面設計 - 隨機抽號系統

本文件根據系統架構與流程圖，定義所有的 Flask 路由、對應的視圖函式及 Jinja2 模板，為前後端實作提供依據。

## 1. 路由總覽表格

| 功能 | HTTP 方法 | URL 路徑 | 對應模板 | 說明 |
| :--- | :--- | :--- | :--- | :--- |
| **首頁** | GET | `/` | `index.html` | 顯示網站介紹與抽籤選項入口 |
| **註冊頁面** | GET | `/auth/register` | `auth/register.html` | 顯示註冊表單 |
| **執行註冊** | POST | `/auth/register` | — | 接收註冊表單，存入 DB，重導向至登入頁 |
| **登入頁面** | GET | `/auth/login` | `auth/login.html` | 顯示登入表單 |
| **執行登入** | POST | `/auth/login` | — | 驗證帳密，設定 Session，重導向至首頁 |
| **登出系統** | GET | `/auth/logout` | — | 清除 Session，重導向至首頁 |
| **數字抽籤設定** | GET | `/draw/number` | `draw/setup_number.html` | 顯示數字範圍與抽出數量設定表單 |
| **執行數字抽籤** | POST | `/draw/number` | — | 執行抽籤，存入紀錄，重導向至結果頁 |
| **名單抽籤設定** | GET | `/draw/custom` | `draw/setup_custom.html` | 顯示自訂名單輸入表單（可選取已存名單） |
| **執行名單抽籤** | POST | `/draw/custom` | — | 執行名單抽籤，存入紀錄，重導向至結果頁 |
| **顯示抽籤結果** | GET | `/draw/result/<id>` | `draw/result.html` | 根據紀錄 ID 顯示結果 |
| **歷史紀錄** | GET | `/draw/history` | `draw/history.html` | 列出登入使用者過去的抽籤紀錄 |
| **自訂名單管理** | GET | `/draw/lists` | `draw/lists.html` | 列出已儲存的自訂名單 |
| **新增自訂名單** | POST | `/draw/lists/new` | — | 從表單接收名單資料，存入 DB，重導向 |
| **刪除自訂名單** | POST | `/draw/lists/<id>/delete`| — | 刪除自訂名單，重導向回管理頁 |

## 2. 每個路由的詳細說明

### `main` Blueprint
- **`/` (GET)**
  - 輸入：無
  - 處理邏輯：單純顯示首頁，判斷是否已登入以顯示不同導覽列。
  - 輸出：渲染 `index.html`。

### `auth` Blueprint
- **`/auth/register` (POST)**
  - 輸入：表單欄位 `username`, `password`, `confirm_password`。
  - 處理邏輯：驗證密碼一致性，檢查帳號是否重複，密碼雜湊後呼叫 `User.create`。
  - 輸出：成功重導至 `/auth/login`，失敗回傳帶有錯誤訊息的 `auth/register.html`。
- **`/auth/login` (POST)**
  - 輸入：表單欄位 `username`, `password`。
  - 處理邏輯：呼叫 `User.get_by_username`，驗證密碼，成功則寫入 session。
  - 輸出：成功重導至 `/`，失敗回傳帶有錯誤訊息的 `auth/login.html`。

### `draw` Blueprint
- **`/draw/number` (POST)**
  - 輸入：表單欄位 `start`, `end`, `count`。
  - 處理邏輯：執行亂數抽取，若已登入則呼叫 `DrawRecord.create` 儲存，取得 `record_id`。若未登入可能存入 session 暫存。
  - 輸出：重導至 `/draw/result/<record_id>`。
- **`/draw/custom` (POST)**
  - 輸入：表單欄位 `items` (逗號分隔或多行文字), `count`。
  - 處理邏輯：將字串轉為 list，執行亂數抽取，若已登入則呼叫 `DrawRecord.create` 儲存。
  - 輸出：重導至 `/draw/result/<record_id>`。
- **`/draw/result/<id>` (GET)**
  - 輸入：URL 參數 `id`。
  - 處理邏輯：呼叫 `DrawRecord.get_by_id` 取得結果。
  - 輸出：渲染 `draw/result.html`。如果找不到紀錄，回傳 404 頁面。

## 3. Jinja2 模板清單

所有頁面預計都會繼承 `base.html`，以共用導覽列 (Navbar) 與頁尾 (Footer)。

- `base.html`：基底版型，引入 CSS/JS，定義 block content。
- `index.html`：網站首頁，提供「數字抽號」與「名單抽號」入口按鈕。
- `auth/register.html`：註冊表單。
- `auth/login.html`：登入表單。
- `draw/setup_number.html`：數字抽籤設定頁。
- `draw/setup_custom.html`：自訂名單設定頁。
- `draw/result.html`：顯示抽出結果（可搭配 JavaScript 動畫）。
- `draw/history.html`：以表格形式列出過去抽籤紀錄。
- `draw/lists.html`：列出並管理（新增/刪除）常用名單。

## 4. 路由骨架程式碼

已在 `app/routes/` 下建立對應的 Python 檔案骨架。
