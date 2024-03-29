from flask import Blueprint, request, jsonify
from firebase_admin import firestore, auth
from helper import create_session
session_api = Blueprint('session_api', __name__)

from flask_cors import CORS, cross_origin

from helper import vision_module

db = firestore.client()
db_ref = db.collection('sessions')

'''
POST /api/session/create

Description: Adds the session id to the users.

JSON response format:
{
"Added Sucessfully
}

JSON error format:
{
    "error": "error message"
}

example JSON request:
{
"user_id": "RX5PRuhgD0cWrc4kby7NVdxJmeB3",
"session_id":"16mEYE1aa5ThDtCFglVO",
"level":"level4"
}
'''

@session_api.route('/add/level/user', methods=['POST'])
@cross_origin()
def add_user_level():
    try:
        user_id = request.json["user_id"]
        session_id = request.json["session_id"]
        level = request.json["level"]
        
        # Retrieve user's current level data
        user_ref = db.collection('users').document(user_id)
        user_data = user_ref.get()
        if not user_data.exists:
            return jsonify({'error': 'User not found'}), 404
        
        user_dict = user_data.to_dict()
        user_level = user_dict.get(level, [])  # Get the existing level array or an empty list
        
        # Add the new session ID to the user's level
        user_level.append(session_id)
        
        # Update the user's level data in the database
        user_ref.update({
            level: user_level
        })
        
        return jsonify("added succesfully"), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400

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
@cross_origin()
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
@cross_origin()
def submit_response():
    try:
        print("mark 1")
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
POST /api/session/userStats

Description: Returns the user's stats for each level.

JSON request format:
{
    "user_id": user_id,
    "level": level,
}

JSON response format:
{
    [
        {
            "attempt": int,
            "average accuracy": accuracy
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
example of user document in database:
{
    "recommended_level": 0,
    "level1": [session_id1, session_id2, ...],
    "level2": [session_id9, session_id10, ...],
    "level3": [],
    "level4": [],
    "level5": []
}
'''
@session_api.route('/userStats', methods=['GET'])
@cross_origin()
def user_stats():
    try:
        user_id = request.json["user_id"]
        user_ref = db.collection('users').document(user_id)
        user_doc = user_ref.get().to_dict()
        level = request.json["level"]
        user_stats = []
        if level == 1:
            level_sessions = user_doc["level1"]
        elif level == 2:
            level_sessions = user_doc["level2"]
        elif level == 3:
            level_sessions = user_doc["level3"]
        elif level == 4:
            level_sessions = user_doc["level4"]
        elif level == 5:
            level_sessions = user_doc["level5"]
        else:
            level_sessions = []

        accuracy = 0
        for session_id in level_sessions:
            session_doc = db_ref.document(session_id).get().to_dict()
            for question in session_doc["questions"]:
                accuracy += question["accuracy"]
            user_stats.append(
                {
                    "attempt": len(session_doc["questions"]),
                    "average accuracy": accuracy/len(session_doc["questions"])
                }
            )
        return jsonify(user_stats), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 400



'''
GET /api/session/placementTest

Description: generates 3 of each level for the user to complete.

JSON request format:
{
    "user_id": user_id,
}

JSON response format:
{
    sessions: 
    [
        {
            "level": level,
            "session_id": session_id,
            prompts: [
                {
                    "prompt": prompt,
                    "overlay": overlay,
                },
                ...
            ]

        },
        ...
    ]
    ]

'''
@session_api.route('/placementTest', methods=['GET'])
@cross_origin()
def placement_test():
    try:
        user_id = request.json["user_id"]

        # generate 5 sessions, one for each level
        for level in range(1, 6):
            # generate 3 prompts for each level
            session_prompts = create_session(level, 3)
            session_id = db_ref.document().id
            db_ref.document(session_id).set({
                "user_id": user_id,
                "questions": [],
                "level": level,
                "amount": 3}
                )
            
            db_ref.document(session_id).update({
                "questions": firestore.ArrayUnion([{
                    "prompt": prompt,
                    "answer": "",
                    "accuracy": 0
                } for prompt in session_prompts])
            })

        # return all sessions
        sessions = []
        for level in range(1, 6):
            sessions.append({
                "level": level,
                "session_id": session_id,
                "prompts": session_prompts
            })

        
        return jsonify({'sessions': sessions}), 200
        
    except Exception as e:
        return jsonify({'error': str(e)}), 400
