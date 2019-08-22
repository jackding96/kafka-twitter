from kafka import KafkaProducer
import threading
import sys
import tweepy
import os

consumer_key = os.environ.get("TWITTER_CONSUMER_KEY")
consumer_secret = os.environ.get("TWITTER_CONSUMER_SECRET")
access_token = os.environ.get("TWITTER_ACCESS_TOKEN")
access_token_secret = os.environ.get("TWITTER_ACCESS_TOKEN_SECRET")

auth = tweepy.OAuthHandler(consumer_key, consumer_secret)
auth.set_access_token(access_token, access_token_secret)

api = tweepy.API(auth)

producer = KafkaProducer(bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'])

class MyStreamListener(tweepy.StreamListener):

  def on_status(self, status):
    print(status.text)
    producer.send('test-multi-broker-topic', status.text.encode('utf-8'))

twitter_streamer = MyStreamListener()
twitter_stream = tweepy.Stream(auth=api.auth, listener=twitter_streamer)
twitter_stream.filter(track=["coffee"], is_async=True)


