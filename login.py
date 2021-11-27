from connect_db import get_db


def validate_user(username, password):
    con = get_db()
    cur = con.cursor()
    query = """
        SELECT * FROM passwords WHERE username = ? AND password = ?;
    """
    return cur.execute(query, [username, password]).fetchone()

