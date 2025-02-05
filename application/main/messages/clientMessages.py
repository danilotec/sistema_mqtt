from functools import cache
from application.models.messageSchema import DeviceData
from datetime import datetime
from sqlalchemy.orm import Session

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

