from app.models.db import get_db_connection

class Activity:
    @staticmethod
    def create(name):
        """建立新的抽籤活動"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO activities (name) VALUES (?)", (name,))
        conn.commit()
        activity_id = cursor.lastrowid
        conn.close()
        return activity_id

    @staticmethod
    def get_all():
        """取得所有建立的抽籤活動"""
        conn = get_db_connection()
        activities = conn.execute("SELECT * FROM activities ORDER BY created_at DESC").fetchall()
        conn.close()
        return activities

    @staticmethod
    def get_by_id(activity_id):
        """根據 ID 取得特定活動資料"""
        conn = get_db_connection()
        activity = conn.execute("SELECT * FROM activities WHERE id = ?", (activity_id,)).fetchone()
        conn.close()
        return activity

    @staticmethod
    def delete(activity_id):
        """刪除抽籤活動"""
        conn = get_db_connection()
        conn.execute("DELETE FROM activities WHERE id = ?", (activity_id,))
        conn.commit()
        conn.close()
