from app.models.db import get_db_connection

class Candidate:
    @staticmethod
    def create(activity_id, name):
        """建立單一候選項目"""
        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO candidates (activity_id, name) VALUES (?, ?)", (activity_id, name))
        conn.commit()
        candidate_id = cursor.lastrowid
        conn.close()
        return candidate_id

    @staticmethod
    def create_many(activity_id, names):
        """建立多個候選項目"""
        if not names:
            return
        conn = get_db_connection()
        cursor = conn.cursor()
        data = [(activity_id, name) for name in names]
        cursor.executemany("INSERT INTO candidates (activity_id, name) VALUES (?, ?)", data)
        conn.commit()
        conn.close()

    @staticmethod
    def get_by_activity_id(activity_id):
        """取得特定活動下的所有候選名單"""
        conn = get_db_connection()
        candidates = conn.execute("SELECT * FROM candidates WHERE activity_id = ? ORDER BY id ASC", (activity_id,)).fetchall()
        conn.close()
        return candidates

    @staticmethod
    def get_undrawn_by_activity(activity_id):
        """取得特定活動下尚未被抽出的候補名單"""
        conn = get_db_connection()
        candidates = conn.execute("SELECT * FROM candidates WHERE activity_id = ? AND is_drawn = 0", (activity_id,)).fetchall()
        conn.close()
        return candidates
        
    @staticmethod
    def get_drawn_by_activity(activity_id):
        """取得特定活動下已經被抽出的名單"""
        conn = get_db_connection()
        candidates = conn.execute("SELECT * FROM candidates WHERE activity_id = ? AND is_drawn = 1 ORDER BY id DESC", (activity_id,)).fetchall()
        conn.close()
        return candidates

    @staticmethod
    def mark_as_drawn(candidate_ids):
        """將名單標記為已抽出"""
        if not candidate_ids:
            return
        conn = get_db_connection()
        placeholders = ','.join('?' for _ in candidate_ids)
        conn.execute(f"UPDATE candidates SET is_drawn = 1 WHERE id IN ({placeholders})", tuple(candidate_ids))
        conn.commit()
        conn.close()
        
    @staticmethod
    def reset_drawn_status(activity_id):
        """重置活動中所有人的成未抽出狀態"""
        conn = get_db_connection()
        conn.execute("UPDATE candidates SET is_drawn = 0 WHERE activity_id = ?", (activity_id,))
        conn.commit()
        conn.close()
