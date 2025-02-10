import os
from dotenv import load_dotenv

load_dotenv()

class Config:
    def __init__(self):
        self.host = str(os.getenv('HOST'))
        self.port = int(os.getenv('PORT'))
        self.clientname = str(os.getenv('CLIENT_NAME'))
        self.username = str(os.getenv('USERNAME_MQTT'))
        self.password = str(os.getenv('PASSWORD_MQTT'))
        self.keepalive = int(os.getenv('KEEPALIVE'))
        self.topics = str(os.getenv('TOPICS'))

class ConfigDatabase:
    database_uri = str(os.getenv('SQLALCHEMY_DATABASE_URI'))
    SQLALCHEMY_TRACK_MODIFICATIONS = False

