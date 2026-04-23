from flask import render_template, request, redirect, url_for, session, flash
from app.routes import auth_bp
# from app.models.user import User

@auth_bp.route('/register', methods=['GET', 'POST'])
def register():
    """
    處理使用者註冊。
    GET: 渲染 'auth/register.html' 表單。
    POST: 接收表單資料，驗證後建立新使用者，重導向到登入頁。
    """
    pass

@auth_bp.route('/login', methods=['GET', 'POST'])
def login():
    """
    處理使用者登入。
    GET: 渲染 'auth/login.html' 表單。
    POST: 驗證帳號密碼，成功後寫入 session，重導向到首頁。
    """
    pass

@auth_bp.route('/logout')
def logout():
    """
    處理登出。
    清除 session，重導向到首頁。
    """
    pass
