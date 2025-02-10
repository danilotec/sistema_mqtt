from functools import cache
from application.models.messageSchema import DeviceData
from datetime import datetime
from sqlalchemy.orm import Session
from flask import jsonify
@cache
class MessagesTopicsData:
    def __init__(self, topic, message) -> None:
        self.topic = topic
        self.message = message
        self.devicedata = None

    def add_message_db(self, db: Session):
        print('Menssagem recebida!')
        print(self.topic)
        print(self.message)
        self.devicedata = DeviceData(
            topic=self.topic,
            payload=self.message,
            create_in=datetime.now()
        )
        db.add(self.devicedata)
        db.commit()
        db.refresh(self.devicedata)
        db.close()
        return self.devicedata
    

    def get_messages_db(self, db: Session):
        messages = db.query(DeviceData).all()
        messages_list = [
            {"id": msg.id, "topic": msg.topic, "payload": msg.payload, "create_in": msg.create_in.isoformat()}
            for msg in messages
        ]
        return jsonify(messages_list)
