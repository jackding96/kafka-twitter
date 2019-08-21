from kafka import KafkaConsumer

consumer = KafkaConsumer( 'test-multi-broker-topic',
                          bootstrap_servers=['localhost:9092', 'localhost:9093', 'localhost:9094'])
for message in consumer:
    print (message.value.decode("utf-8") )