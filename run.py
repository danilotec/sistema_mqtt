from application.main.main import start
from application.database.createTables import create_tables
if __name__ == "__main__":
    create_tables()
    start()