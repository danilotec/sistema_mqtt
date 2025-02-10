from application.main.main import start
from application.database.createTables import create_tables
from application.api.app import run_flask
import threading

if __name__ == "__main__":
    create_tables()

    flask_thread = threading.Thread(target=run_flask)
    flask_thread.start()

    start()