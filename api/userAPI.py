from flask import Blueprint, request, jsonify
from firebase_admin import firestore, auth

user_api = Blueprint('user_api', __name__)

db = firestore.client()
users_ref = db.collection('users')



'''
POST /api/user/register

Description: Registers a new user in the database.

JSON request format:
{
    "email": "user email",
    "password": "user key",
    "email_verified": boolean,
    "account_disabled": boolean
}

JSON response format:
{
    "uid": "user id"
}

JSON error format:
{
    "error": "error message"
}
'''
@user_api.route('/register', methods=['POST'])
def register():
    try:
        user = request.json
        user = auth.create_user(
            email=user['email'],
            password=user['password'],
            email_verified=user['email_verified'],
            disabled=user['account_disabled']
        )
        return jsonify({'uid': user.uid}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

'''
POST /api/user/login_with_google

Description: Logs in a user with a Google account.

JSON request format:
{
    "id_token": "user id token"
}

JSON response format:
{
    "uid": "user id"
}

JSON error format:
{
    "error": "error message"
}
'''
@user_api.route('/login_with_google', methods=['POST'])
def login_with_google():
    try:
        user = request.json
        user = auth.verify_id_token(user['id_token'])
        return jsonify({'uid': user['uid']}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400



'''
POST /api/user/login

Description: Logs in a user.

JSON request format:
{
    "email": "user email",
    "password": "user key"
}

JSON response format:
{
    "uid": "user id"
}

JSON error format:
{
    "error": "error message"
}

'''
@user_api.route('/login', methods=['POST'])
def login():
    try:
        user = request.json
        user = auth.get_user_by_email(user['email'])
        return jsonify({'uid': user.uid}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    
'''
GET /api/user/<uid>

Description: Gets a user's information.

JSON response format:
{
    "email": "user email",
    "email_verified": boolean,
    "account_disabled": boolean
}

JSON error format:
{
    "error": "error message"
}
'''
@user_api.route('/<uid>', methods=['GET'])
def get_user(uid):
    try:
        user = auth.get_user(uid)
        return jsonify({
            'email': user.email,
            'email_verified': user.email_verified,
            'account_disabled': user.disabled
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400




