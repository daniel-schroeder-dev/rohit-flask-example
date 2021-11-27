from connect_db import get_db


def get_user(user_id):
    con = get_db()
    cur = con.cursor()
    query = """
        SELECT * FROM passwords WHERE id = ?;
    """
    return cur.execute(query, [user_id]).fetchone()