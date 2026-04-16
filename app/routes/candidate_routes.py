from flask import Blueprint, request, redirect, url_for, flash, render_template
import random

candidate_bp = Blueprint('candidate', __name__)

@candidate_bp.route('/activities/<int:activity_id>/candidates', methods=['POST'])
def add_candidates(activity_id):
    """
    [POST] 新增多筆候選名單
    讀取 textarea 表單，以換行切割後批次建立，重導向回活動管理頁
    """
    pass

@candidate_bp.route('/activities/<int:activity_id>/draw', methods=['POST'])
def draw_candidates(activity_id):
    """
    [POST] 執行抽籤
    依據請求的數量 (draw_count)，從未抽籤名單中隨機選擇 N 個
    標記這些人為被抽出狀態 (is_drawn = 1)
    然後將結果傳給 activities/draw_result.html 進行渲染展示
    """
    pass

@candidate_bp.route('/activities/<int:activity_id>/reset', methods=['POST'])
def reset_candidates(activity_id):
    """
    [POST] 重置所有名單狀態
    將特定活動下的所有人 is_drawn 設為 0
    完成後重導向回活動管理頁
    """
    pass
