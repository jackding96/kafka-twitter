from kafka import KafkaProducer
import threading
import sys

producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'])

def sendMessage(count, prod):
  producer.send('test-multi-broker-topic', f"{prod}: Message {count}".encode("utf-8"))
  print(f"{prod}: Message {count}")
  threading.Timer(1.0, sendMessage, [count+1, prod]).start()

sendMessage(1, sys.argv[1])