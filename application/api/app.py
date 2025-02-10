from flask import Flask, jsonify
from application.main.messages.clientMessages import MessagesTopicsData
from application.database.base import SessionLocal

app = Flask(__name__)

@app.route("/data", methods=['GET'])
def hello_world():
    db = SessionLocal()
    message_database = MessagesTopicsData('.', '.')
    data = message_database.get_messages_db(db)
    print(data)
    return data

def run_flask():
    app.run(debug=True, use_reloader=False)