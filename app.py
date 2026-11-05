from flask import Flask, render_template, request, jsonify
from agent import ask_agent

# Initialize Flask application
app = Flask(__name__)


# Homepage route
@app.route("/")
def home():
    return render_template("index.html")


# Chatbot API endpoint
@app.route("/chat", methods=["POST"])
def chat():

    try:

        data = request.get_json()

        user_message = data.get("message", "").strip()

        if not user_message:
            return jsonify({
                "error": "Please enter a message."
            }), 400

        # Send message to AI agent
        ai_response = ask_agent(user_message)

        return jsonify({
            "response": ai_response
        })

    except Exception as e:

        print("Error:", str(e))

        return jsonify({
            "error": "AI assistant is temporarily unavailable."
        }), 500


# Run application
if __name__ == "__main__":

    app.run(
        debug=True,
        port=5000
    )