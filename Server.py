from flask_cors import CORS, cross_origin
import json
import os
from database import *
from user_data import *
from flask import Flask, json, request, jsonify
app = Flask(__name__, static_folder="frontend/build")
# This is the code for all the routes


@app.route("/")
def home():
    return "Hello world"


@app.route("/data", methods=['POST'])
@cross_origin()
def members():
    request_data = json.loads(request.data)
    CREATE_DATABASE()
    ADDING_NEW_ELEMENT(request_data)
    PRINTING_SINGLE_ITEM()

    return (" ")


@app.route("/signup", methods=['POST'])
@cross_origin()
def Signup_Data():
    request_data = json.loads(request.data)
    create_table_user()
    insert_table_user(request_data)

    return (" ")


@app.route("/login_add", methods=['POST'])
@cross_origin()
def Login_Data():
    global check_user
    check_user = False
    request_data = json.loads(request.data)
    check_user = get_data(request_data)

    return ('')


@app.route("/login_send", methods=['GET'])
@cross_origin()
def Login_Data_Send():
    print({"state": [str(check_user)]})
    return {"state_type": [str(check_user)]}


if __name__ == '__main__':
    app.run(debug=True)
