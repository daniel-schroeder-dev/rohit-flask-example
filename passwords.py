from connect_db import get_db


def update_column(column_name, username, column_value):
    con = get_db()
    cur = con.cursor()
    
    query = """
        SELECT * FROM passwords;
    """
    cur.execute(query)
    valid_column_names = [data[0] for data in cur.description if data[0] != "id"]
    
    if column_name in valid_column_names:
        query = f"""
            UPDATE passwords SET {column_name} = ? WHERE username = ?;
        """
        cur.execute(query, [column_value, username])
        con.commit()