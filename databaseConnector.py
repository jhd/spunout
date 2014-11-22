import sqlite3
from flask import g

DATABASE = 'spunout.sqlite'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('spunout.sqlite3')
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

def get_all():
    data = query_db('select * from responces', one = False)
    return data

def get_user(user_id):
    user = query_db('select * from users where email = ?', [user_id], one=True)
    if user is None:
        return None
    else:
        return user

def get_responce(responce_id):
    responce = query_db('select * from responces where responce_id = ?', [responce_id], one=True)
    if responce is None:
        return None
    else:
        return responce

def get_responces(user_id):
    responce = query_db('select * from responces where email = ?', [user_id], one = False)
    if responce is None:
        return None
    else:
        return responce

def post_responce(email,question_id,datetime,response):
    data = [email,question_id,datetime,response]
    responce = query_db('insert into responces values (2,?,?,?,?);', data )
    return responce