#!flask/bin/python
from app import app
from flask import Flask, jsonify,request
from databaseConnector import get_user

fakedata = [
    {
        'user_id': 1,
        'question_id' : 2,
        'datetime' : u'2014/12/26',
        'response' : u'WAT'
    }
]
@app.route('/')
@app.route('/index')
def index():
    return "Hello, World!"

# retuns all data in the database
@app.route('/api/getalldata', methods=['GET'])
def getalldata():
    return str(1)
# returns a single users data 
@app.route('/api/getuserdata/<int:user_id>', methods=['GET'])
def getdataforuser(user_id):
    return get_user(user_id)
#push user data to database
@app.route('/api/putdata/<int:user_id>', methods=['POST'])
def putdataforuser(user_id):
    return str(1)