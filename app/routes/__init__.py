from flask import Blueprint

# 初始化各個 Blueprint
main_bp = Blueprint('main', __name__)
auth_bp = Blueprint('auth', __name__, url_prefix='/auth')
draw_bp = Blueprint('draw', __name__, url_prefix='/draw')

# 匯入各個路由模組以註冊路由
from app.routes import main, auth, draw
