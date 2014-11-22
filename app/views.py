#!flask/bin/python
from app import app
from flask import Flask, jsonify,request

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
	return jsonify({'alldata' : fakedata})

# returns a single users data 
@app.route('/api/getuserdata/<int:user_id>', methods=['GET'])
def getdataforuser(user_id):
	return "some user data for " + str(user_id)

#push user data to database
@app.route('/api/putdata/<int:user_id>', methods=['POST'])
def putdataforuser(user_id):
	q_id = request.form['question_id']
	return str(user_id)