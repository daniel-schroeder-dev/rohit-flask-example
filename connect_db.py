import sqlite3
from flask import g

DATABASE = 'passwords.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect(DATABASE)
        # Let's you access results like a dict
        db.row_factory = sqlite3.Row
    return db