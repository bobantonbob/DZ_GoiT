import redis

r = redis.Redis(host="localhost", port=6379, password=None)

redis_connection = r.pubsub()
r.publish("alpha-1", "Hi, I'm in...")

redis_connection.subscribe("alpha-1")

for message in redis_connection.listen():
    print(message)
