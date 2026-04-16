import sqlite3
import os

DB_PATH = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'app.db')

def get_db_connection():
    """取得資料庫連線"""
    conn = sqlite3.connect(DB_PATH)
    # 將查詢結果包裝為類似字典的存取方式
    conn.row_factory = sqlite3.Row
    return conn

def init_db():
    """初始化資料庫（首次執行時）"""
    schema_path = os.path.join(os.path.dirname(os.path.dirname(os.path.dirname(__file__))), 'database', 'schema.sql')
    if not os.path.exists(schema_path):
        return
        
    # 如果 database 目錄不存在則建立
    os.makedirs(os.path.dirname(DB_PATH), exist_ok=True)
        
    with open(schema_path, 'r', encoding='utf-8') as f:
        schema_sql = f.read()
        
    conn = get_db_connection()
    conn.executescript(schema_sql)
    conn.commit()
    conn.close()
