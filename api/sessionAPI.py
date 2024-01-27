from flask import Blueprint, request, jsonify
from firebase_admin import firestore, auth
from helper import create_session
session_api = Blueprint('session_api', __name__)

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

example JSON request:
{
    "user_id": "test",
    "level": 1,
    "amount": 3
}
'''
@session_api.route('/create', methods=['POST'])
def create_session_api():
    try:
        user_id = request.json["user_id"]
        level = request.json["level"]
        amount = request.json["amount"]
        session_id = db_ref.document().id
        prompts = create_session(level, amount)

        db_ref.document(session_id).set({
            "user_id": user_id,
            "questions": [],
            "level": level,
            "amount": amount}
            )
            
        return jsonify({'session_id': session_id, 'prompts': prompts}), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400


'''
POST /api/session/submit

Description: Submits each user response to the database and returns accuracy, this submission is done after each prompt.

JSON request format:
{
    "session_id": session_id,
    "user_id": user_id,
    "question":
    {
        "prompt": prompt,
        "answer": answer,
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
@session_api.route('/submit', methods=['POST'])
def submit_response():
    try:
        session_id = request.json["session_id"]

        question = request.json["question"]
        prompt = question["prompt"]
        answer = question["answer"]
    
        # use vision_module(question, answer) to get accuracy for prompt and save it to the database
        accuracy = vision_module(question, answer)

        # append accuracy, prompt, and response to the list "questions" in the session document
        db_ref.document(session_id).update({
            "questions": firestore.ArrayUnion([{
                "prompt": prompt,
                "answer": answer,
                "accuracy": accuracy
            }])
        })
    except Exception as e:
        return jsonify({'error': str(e)}), 400
    

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
