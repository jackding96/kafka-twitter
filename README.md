# kafka-twitter

Playing around with Kafka, Python, Flink (Maybe) and the Twitter API, trying to set up a data pipeline that does continuous sentiment analysis on real-time tweets.

### Setup: Running Kafka on Local Machine
0. Navigate to Kafka folder
1. Start the Zookeeper server by running: `bin/zookeeper-server-start.sh config/zookeeper.properties`
2. Start Kafka broker(s) by running: `bin/kafka-server-start.sh config/{BROKER_CONFIG_FILE}`, where "BROKER_CONFIG_FILE" is each broker's properties file
3. Run `jps` to verify that Zookeeper ("QuorumPeerMain") / Kafka broker instances are running as expected