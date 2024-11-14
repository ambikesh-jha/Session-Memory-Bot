from flask import Flask, render_template, request, jsonify
from chatbot import Chatbot
from history import History

app = Flask(__name__)
chatbot = Chatbot()
history = History()

@app.route("/")
def index():
    return render_template("chat.html")

@app.route("/chat", methods=["POST"])
def chat():
    user_input = request.json.get("message")
    history.add_message("User", user_input)
    bot_response = chatbot.get_response(user_input)
    history.add_message("Bot", bot_response)
    return jsonify({
        "user_input": user_input,
        "bot_response": bot_response,
        "history": history.get_history()
    })

if __name__ == "__main__":
    app.run(debug=True)







