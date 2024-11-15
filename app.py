from flask import Flask, render_template, request, jsonify, session
from flask_session import Session
from database import mongo, save_message, get_chat_history
from session_config import get_session_id
from chatbot import Chatbot
from history import History

app = Flask(__name__)

# MongoDB and Flask-Session configuration
app.config["MONGO_URI"] = "mongodb://localhost:27017/smartbot_db"  # Update with your MongoDB URI
app.config["SESSION_TYPE"] = "filesystem" 
Session(app)
mongo.init_app(app)

chatbot = Chatbot()
history = History()

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    session_id = get_session_id()

    # Save user message to MongoDB
    save_message(session_id, "User", user_input)
    processed_input = f"'{user_input}' give to the point answer"
    history.add_message("User", user_input)

    # Get bot response
    bot_response = chatbot.get_response(processed_input)
    save_message(session_id, "Bot", bot_response)
    history.add_message("Bot", bot_response)

    return jsonify({
        "user_input": user_input,
        "bot_response": bot_response,
        "history": history.get_history()
    })

@app.route("/history", methods=["GET"])
def get_history():
    session_id = get_session_id()
    chat_history = get_chat_history(session_id)
    return jsonify(chat_history)

if __name__ == "__main__":
    app.run(debug=True)

