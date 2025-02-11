from flask import Flask, jsonify
from application.main.messages.clientMessages import MessagesTopicsData
from application.database.base import SessionLocal
from application.api.admin import require_api_key

app = Flask(__name__)

@app.route('/')
@require_api_key
def index():
    return jsonify({'Access successful': 'Wellcome!'})

@app.route("/data", methods=['GET'])
@require_api_key
def monitor_data():
    db = SessionLocal()
    message_database = MessagesTopicsData('.', '.')
    data = message_database.get_messages_db(db)
    print(data)
    return data

@app.route("/delete", methods=['DELETE'])
@require_api_key
def delete_data():
    db = SessionLocal()
    message_database = MessagesTopicsData('.', '.')
    data = message_database.delete_all_messages(db)
    return data

def run_flask():
    app.run(debug=True, use_reloader=False)