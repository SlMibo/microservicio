from database import Base
from sqlalchemy import Column, String, Integer, Float, DateTime, ForeignKey, Text
from sqlalchemy.orm import relationship
import json
from datetime import datetime

class Event(Base):
    __tablename__ = 'events'

    id = Column(Integer, primary_key=True, index=True)
    event_type = Column(String, index=True)
    payload = Column(Text)
    timestamp = Column(DateTime, default=datetime.utcnow)

    def to_dict(self):
        return {
            "id": self.id,
            "event_type": self.event_type,
            "payload": json.loads(self.payload),
            "timestamp": self.timestamp,
        }

class User(Base):
    __tablename__ = "users"

    id = Column(Integer,primary_key=True,nullable=False,autoincrement=True)
    name = Column(String,nullable=False)
    surname = Column(String,nullable=False)
    email = Column(String,nullable=False)
    password = Column(String,nullable=False)