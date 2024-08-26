from kafka import KafkaConsumer
import json
from sqlalchemy.orm import Session
from .database import SessionLocal
from . import models

consumer = KafkaConsumer(
    'object-events',
    bootstrap_servers=['localhost:9092'],
    auto_offset_reset='earliest',
    enable_auto_commit=True,
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def consume_events():
    db: Session = SessionLocal()
    for message in consumer:
        event = json.loads(message.value)
        if event["event_type"] == "UserCreated":
            projection = models.User(**event["payload"])
            db.add(projection)
        # elif event["event_type"] == "UserUpdated":
        #     projection = db.query(models.User).filter(models.User.id == event["payload"]["id"]).first()
        #     if projection:
        #         for key, value in event["payload"].items():
        #             setattr(projection, key, value)
        db.commit()
