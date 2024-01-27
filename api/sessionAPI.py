from flask import Blueprint, request, jsonify
from firebase_admin import firestore, auth

database_api = Blueprint('session_api', __name__)

db = firestore.client()
db_ref = db.collection('levels')

'''
POST /api/session/create

Description: Creates a new session which generates a batch of user prompts.

JSON request format:
{
    "user_id": user_id,
    "level": level,
    "amount": amount
}

JSON response format:
{
    "session_id": session_id,
    prompts: [
        {
            "prompt": prompt,
            "overlay": overlay,
        },
        ...
    ]
}

JSON error format:
{
    "error": "error message"
}

'''



'''
POST /api/session/submit

Description: Submits each user response to the database and returns accuracy.

JSON request format:
{
    "session_id": session_id,
    "user_id": user_id,
    "response":
    {
        "prompt": prompt,
        "response": response,
    },
}

JSON response format:
{
    "accuracy": accuracy
}

JSON error format:
{
    "error": "error message"
}
'''

'''
GET /api/session/userStats

Description: Returns the user's stats for each level.

JSON request format:
{
    "user_id": user_id,
}

JSON response format:
{
    "level": level,
    "accuracy": accuracy
}

JSON error format:
{
    "error": "error message"
}

'''

'''
GET /api/session/placementTest

Description: generates 3 of each level for the user to complete.

JSON request format:
{
    "user_id": user_id,
    "session_id": session_id,
}

JSON response format:
{
    prompts: 
    [
        {
            "level": level,
            "prompt": prompt,
            "overlay": overlay,
        },
        ...
    ]
    ]

'''