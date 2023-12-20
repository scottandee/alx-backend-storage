#!/usr/bin/env python3
"""This script contains the Cache class"""

import redis
import uuid


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
