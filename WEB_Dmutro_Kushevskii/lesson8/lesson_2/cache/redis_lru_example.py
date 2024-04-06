import time
import redis
import redis_lru
import datetime


client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = redis_lru.RedisLRU(client)

start = datetime.datetime.now() + datetime.timedelta(seconds=1)

@cache(expire_on=start)
def f(x):
    print(f"Function call f({x})")
    return x


if __name__ == '__main__':
    print(f"Result f(5): {f(5)}")
    time.sleep(1)
    print(f"Result f(5): {f(5)}")
    print(f"Result f(5): {f(5)}")
