from sqlalchemy import Column, Integer, String, DateTime
from application.database.base import Base


class DeviceData(Base):
    __tablename__ = 'Devices'

    id = Column(Integer, primary_key=True)
    topic = Column(String)
    payload = Column(String)
    create_in = Column(DateTime)