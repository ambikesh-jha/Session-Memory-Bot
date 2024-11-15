from flask_pymongo import PyMongo

mongo = PyMongo()

def save_message(session_id, sender, message):
    mongo.db.chat_history.insert_one({
        "session_id": session_id,
        "sender": sender,
        "message": message
    })

def get_chat_history(session_id):
    messages = mongo.db.chat_history.find({"session_id": session_id})
    return [{"sender": msg["sender"], "message": msg["message"]} for msg in messages]

