import os
from flask import Flask, send_file
from firebase_admin import credentials, firestore, initialize_app
from flask import Blueprint, request, jsonify

from flask_cors import CORS, cross_origin
app = Flask(__name__)
cors = CORS(app)
app.config['CORS_HEADERS'] = 'Content-Type'

cur_path = os.path.dirname(os.path.realpath(__file__))
cred = credentials.Certificate(f"{cur_path}/key.json")
default_app = initialize_app(cred)

app = Flask(__name__)
from userAPI import user_api
from sessionAPI import session_api

# create a route to test the API
@app.route('/test')
@cross_origin()
def test():
    return 'API is working!'

# test for json data
@app.route('/test/json', methods=['POST'])
@cross_origin()
def test_json_packet():
    print(request.json)
    return jsonify(request.json)

    

app.register_blueprint(user_api, url_prefix='/api/user')
app.register_blueprint(session_api, url_prefix='/api/session')

if __name__ == '__main__':
    app.run(debug=True)