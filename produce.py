#coding=utf-8
from pykafka import KafkaClient
import codecs
import logging

logging.basicConfig(level = logging.INFO)

client = KafkaClient(hosts = "127.0.0.1:9092")

topicdocu = client.topics['test']
producer = topicdocu.get_producer()
for i in range(100):
    message = "this" + str(i+23)
    producer.produce(bytes(message, encoding='utf-8'))
producer.stop()