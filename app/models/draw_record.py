from app.models.db import get_db_connection

class DrawRecord:
    @staticmethod
    def create(user_id, draw_type, settings, result):
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute(
            'INSERT INTO draw_records (user_id, draw_type, settings, result) VALUES (?, ?, ?, ?)',
            (user_id, draw_type, settings, result)
        )
        conn.commit()
        record_id = cursor.lastrowid
        conn.close()
        return record_id

    @staticmethod
    def get_by_user(user_id):
        conn = get_db_connection()
        records = conn.execute('SELECT * FROM draw_records WHERE user_id = ? ORDER BY created_at DESC', (user_id,)).fetchall()
        conn.close()
        return [dict(row) for row in records]

    @staticmethod
    def get_by_id(record_id):
        conn = get_db_connection()
        record = conn.execute('SELECT * FROM draw_records WHERE id = ?', (record_id,)).fetchone()
        conn.close()
        return dict(record) if record else None
