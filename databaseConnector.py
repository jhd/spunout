import sqlite3
from flask import g

DATABASE = 'spunout.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('spunout.sqlite')
    return db

#@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

def query_db(query, args=(), one=False):
     cur = get_db().execute(query, args)
     rv = cur.fetchall()
     cur.close()
     return (rv[0] if rv else None) if one else rv

def get_user(user_id):
    user = query_db('select * from users where user_id = ?', [user_id], one=True)
    if user is None:
        return None
    else:
        return user

def get_responce(reponce_id):
    responce = query_db('select * from responces where responce_id = ?', [responce_id], one=True)
    if responce is None:
        return None
    else:
        return responce

def get_responces(user_id):
    responces = query_db('select * from responces where user_id = ?', [user_id], One = False)
    if responce is None:
        return None
    else:
        return responce
