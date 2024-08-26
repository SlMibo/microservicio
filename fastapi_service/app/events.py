from kafka import KafkaProducer
import json

producer = KafkaProducer(
    bootstrap_servers=['localhost:9092'],
    value_serializer=lambda v: json.dumps(v).encode('utf-8')
)

def publish_event(event_type: str, payload: dict):
    event = {"event_type": event_type, "payload": payload}
    producer.send('object-events', value=event)
    producer.flush()