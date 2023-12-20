#!/usr/bin/env python3
"""This script contains the Cache class"""

import redis
import uuid
from typing import Callable


class Cache:
    """This is the cache class"""

    def __init__(self) -> None:
        """This is the instance method that creates
        a new Redis instance and flushes the db
        """
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: int | float | bytes | str) -> str:
        """This method adds a new key, value pair
        to the redis database
        """
        key: str = str(uuid.uuid4())
        self._redis.set(key, data)
        return key

    def get(self, key: str, fn: Callable = None) -> int | float | bytes | str:
        """This method that retreives the data back in the
        original format in which it was stored
        """
        if not self._redis.exists(key):
            return None
        if fn is None:
            return self._redis.get(key)
        else:
            return fn(self._redis.get(key))

    def get_int(self, key: str) -> int:
        """This ethod retrieves the data back as and
        integer
        """
        if not self._redis.exists(key):
            return None
        return int(self._redis.get(key))

    def get_str(self, key: str) -> str:
        """This ethod retrieves the data back as and
        string
        """
        if not self._redis.exists(key):
            return None
        return str(self._redis.get(key))
