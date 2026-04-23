from flask import render_template
from app.routes import main_bp

@main_bp.route('/')
def index():
    """
    處理首頁請求。
    輸入: 無
    邏輯: 顯示系統介紹、主要功能的入口按鈕（數字抽號、名單抽號）。
    輸出: 渲染 'index.html'
    """
    pass
