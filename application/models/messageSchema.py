from sqlalchemy import Column, Integer, String, DateTime, func
from application.database.base import Base


class DeviceData(Base):
    __tablename__ = 'Devices'

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    payload = Column(String)
    create_in = Column(DateTime, default=func.now(), onupdate=func.now()) #type: ignore

    @classmethod
    def upsert_device(cls, session, topic, payload):
        
        device = session.query(cls).filter_by(topic=topic).first()
        
        if device:
            device.payload = payload
        else:
            device = cls(topic=topic, payload=payload)
            session.add(device)
        
        return device