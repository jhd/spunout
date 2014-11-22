#!flask/bin/python
from app import app
from flask import Flask, jsonify,request, make_response
from databaseConnector import get_user, get_all, get_responce, get_responces    

def no_data_found(message):
    return make_response(jsonify({'error': message }), 400)

@app.route('/')
@app.route('/index')
def index():
    return "Whoop whoop!"

# retuns all data in the database
@app.route('/api/getalldata', methods=['GET'])
def getalldata():
    data = get_all()
    if data is None:
        return no_data_found("No data found at all")
    else:
        return data

@app.route('/api/getuserdata/<string:user_email>', methods=['GET'])
def getdataforuser(user_email):
    data = get_user(user_email)
    if data is None:
        return no_data_found("No data found for " + user_email)
    else:
        return data

@app.route('/api/getresponce/<string:responce_id>', methods=['GET'])
def getresponse(responce_id):
    data = get_responce(responce_id)
    if data is None:
        return no_data_found("No data found for" + responce_id)
    else:
        return data

@app.route('/api/getresponces/<string:user_email>', methods=['GET'])
def getresponses(user_email):
    data = get_responces(user_email)
    if data is None:
        return no_data_found("No response data found for" + user_email)
    else:
        return data
