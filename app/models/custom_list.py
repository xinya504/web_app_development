from app.models.db import get_db_connection

class CustomList:
    @staticmethod
    def create(user_id, title, items):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO custom_lists (user_id, title, items) VALUES (?, ?, ?)',
            (user_id, title, items)
        )
        conn.commit()
        list_id = cursor.lastrowid
        conn.close()
        return list_id

    @staticmethod
    def get_by_user(user_id):
        conn = get_db_connection()
        lists = conn.execute('SELECT * FROM custom_lists WHERE user_id = ? ORDER BY created_at DESC', (user_id,)).fetchall()
        conn.close()
        return [dict(row) for row in lists]

    @staticmethod
    def get_by_id(list_id):
        conn = get_db_connection()
        list_data = conn.execute('SELECT * FROM custom_lists WHERE id = ?', (list_id,)).fetchone()
        conn.close()
        return dict(list_data) if list_data else None

    @staticmethod
    def delete(list_id):
        conn = get_db_connection()
        conn.execute('DELETE FROM custom_lists WHERE id = ?', (list_id,))
        conn.commit()
        conn.close()
