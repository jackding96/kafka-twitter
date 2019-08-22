from kafka import KafkaProducer
import threading
import sys
import json
import requests

url = "https://stream.twitter.com/1.1/statuses/filter.json"

querystring = {"track":"javascript"}

headers = {
    'Content-Type': "application/x-www-form-urlencoded",
    'Authorization': "OAuth oauth_consumer_key=\"Ysen3uq4Inu2TvWHaXBQgZ2eP\",oauth_token=\"2959444329-ndNO2oeHLmAtLGCt7htjs1dMYJe7WN6QPVGlaVq\",oauth_signature_method=\"HMAC-SHA1\",oauth_timestamp=\"1566507687\",oauth_nonce=\"VIqWuqwhFXk\",oauth_version=\"1.0\",oauth_signature=\"8oBZ58K%2FIsUP2NfkmEj9LK7H0f4%3D\"",
    'Accept': "*/*",
    'Cache-Control': "no-cache",
    'Host': "stream.twitter.com",
    'Accept-Encoding': "gzip, deflate",
    'Connection': "keep-alive",
    'cache-control': "no-cache"
    }

response = requests.request("GET", url, stream=True, headers=headers, params=querystring)

for line in response.iter_lines():
  if line:
    decoded = line.decode('utf-8')
    print(decoded)

# producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'])

# def sendMessage(count, prod):
#   producer.send('test-multi-broker-topic', f"{prod}: Message {count}".encode("utf-8")).add_callback(print(f"{prod}: Message {count}"))
#   threading.Timer(1.0, sendMessage, [count+1, prod]).start()

# sendMessage(1, sys.argv[1])