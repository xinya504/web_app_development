from flask import Blueprint, render_template, request, redirect, url_for, flash

activity_bp = Blueprint('activity', __name__)

@activity_bp.route('/')
def index():
    """
    [GET] 首頁
    取得所有的抽籤活動並渲染 index.html
    """
    pass

@activity_bp.route('/activities', methods=['POST'])
def create_activity():
    """
    [POST] 建立活動
    接收表單的 name 參數，建立新活動後重導向至活動管理頁(/activities/<id>)
    """
    pass

@activity_bp.route('/activities/<int:activity_id>')
def detail(activity_id):
    """
    [GET] 活動管理頁面
    取得指定的活動，以及其名下未抽出/已抽出的名單
    渲染 activities/detail.html
    """
    pass

@activity_bp.route('/activities/<int:activity_id>/delete', methods=['POST'])
def delete_activity(activity_id):
    """
    [POST] 刪除活動
    刪除特定活動與其所有的名單，重導向回首頁
    """
    pass
