from typing import List, Any

import redis
from redis_lru import RedisLRU

from models import Author, Quote

client = redis.StrictRedis(host="localhost", port=6379, password=None)
cache = RedisLRU(client)


@cache
def find_by_tag(tag: str) -> List[str | None]:
    print(f"Find by tag: {tag}")
    quotes = Quote.objects(tags__iregex=tag)
    result = [q.quote for q in quotes]
    return result


@cache
def find_by_author(author: str) -> List[List[Any]]:
    print(f"Find by author: {author}")
    authors = Author.objects(fullname__iregex=author)
    result = {}
    for a in authors:
        quotes = Quote.objects(author=a)
        result[a.fullname] = [q.quote for q in quotes]
    return result


if __name__ == '__main__':
    while True:
        command = input("Enter command: ").strip()
        if command.lower() == 'exit':
            break

        parts = command.split(':', 1)
        if len(parts) != 2:
            print("Invalid command format. Please use 'name:', 'tag:', or 'tags:'.")
            continue

        key, value = parts
        if key.lower() == 'name':
            result = find_by_author(value.strip())
        elif key.lower() == 'tag':
            result = find_by_tag(value.strip())
        elif key.lower() == 'tags':
            tags = [tag.strip() for tag in value.split(',')]
            result = []
            for tag in tags:
                result.extend(find_by_tag(tag))
            result = list(set(result))  # remove duplicates
        else:
            print("Invalid command. Please use 'name:', 'tag:', or 'tags:'.")
            continue

        print("Result:")
        print(result)
