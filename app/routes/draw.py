from flask import render_template, request, redirect, url_for, session, flash
from app.routes import draw_bp
# from app.models.draw_record import DrawRecord
# from app.models.custom_list import CustomList

@draw_bp.route('/number', methods=['GET', 'POST'])
def draw_number():
    """
    處理數字抽籤。
    GET: 顯示 'draw/setup_number.html' 表單。
    POST: 接收範圍設定，進行亂數抽取，儲存紀錄，重導向至結果頁。
    """
    pass

@draw_bp.route('/custom', methods=['GET', 'POST'])
def draw_custom():
    """
    處理自訂名單抽籤。
    GET: 顯示 'draw/setup_custom.html' 表單。
    POST: 接收名單字串，進行亂數抽取，儲存紀錄，重導向至結果頁。
    """
    pass

@draw_bp.route('/result/<int:record_id>')
def result(record_id):
    """
    顯示特定抽籤紀錄的結果。
    從資料庫取得 record_id 對應的抽籤結果並顯示於 'draw/result.html'。
    """
    pass

@draw_bp.route('/history')
def history():
    """
    顯示使用者的抽籤歷史紀錄。
    需要登入，從資料庫取出該使用者的紀錄清單，渲染 'draw/history.html'。
    """
    pass

@draw_bp.route('/lists')
def manage_lists():
    """
    管理（查看）自訂名單。
    需要登入，取得該使用者的名單並顯示於 'draw/lists.html'。
    """
    pass

@draw_bp.route('/lists/new', methods=['POST'])
def new_list():
    """
    新增自訂名單。
    接收表單資料並儲存至資料庫，重導向回管理列表。
    """
    pass

@draw_bp.route('/lists/<int:list_id>/delete', methods=['POST'])
def delete_list(list_id):
    """
    刪除自訂名單。
    自資料庫中刪除名單，重導向回管理列表。
    """
    pass
