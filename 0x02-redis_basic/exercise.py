#!/usr/bin/env python3
"""This script contains the Cache class"""

import redis
import uuid
from typing import Callable, Union
from functools import wraps


def count_calls(method: Callable) -> Callable:
    """Decorator to count method calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function for counting calls"""
        self._redis.incr(method.__qualname__, 1)
        result = method(self, *args, **kwargs)
        return result
    return wrapper


def call_history(method: Callable) -> Callable:
    """Decorator to store record of method calls"""
    @wraps(method)
    def wrapper(self, *args, **kwargs):
        """Wrapper function for recording calls"""
        self._redis.rpush(method.__qualname__ + ":inputs", str(args))
        result = method(self, *args, **kwargs)
        self._redis.rpush(method.__qualname__ + ":outputs", str(result))
        return result
    return wrapper


class Cache:
    """This is the cache class"""

    def __init__(self) -> None:
        """This is the instance method that creates
        a new Redis instance and flushes the db
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    @count_calls
    @call_history
    def store(self, data: Union[str, bytes, int, float]) -> str:
        """This method adds a new key, value pair
        to the redis database
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> \
            Union[int, float, bytes, str]:
        """This method that retreives the data back in the
        original format in which it was stored
        """
        if not self._redis.exists(key):
            return None
        if fn is None:
            return self._redis.get(key)
        else:
            return fn(self._redis.get(key))

    def get_int(self, key: str) -> Union[int, None]:
        """This ethod retrieves the data back as and
        integer
        """
        if not self._redis.exists(key):
            return None
        return int.from_bytes(self._redis.get(key), "big")

    def get_str(self, key: str) -> Union[str, None]:
        """This ethod retrieves the data back as and
        string
        """
        if not self._redis.exists(key):
            return None
        return str(self._redis.get(key))


def replay(store):
    """This method displays the history of the
    calls of the method passed as argument
    """
    r = redis.Redis()
    call_count = r.get(store.__qualname__).decode("utf-8")
    inputs = r.lrange("{}:inputs".format(store.__qualname__), 0, -1)
    outputs = r.lrange("{}:outputs".format(store.__qualname__), 0, -1)

    print(f"Cache.store was called {call_count} times:")
    for value, key in zip(inputs, outputs):
        print(f"Cache.store(*{value.decode('utf-8')}) -> \
{key.decode('utf-8')}")
