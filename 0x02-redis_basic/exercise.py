#!/usr/bin/env python3
"""Redis db"""
import redis
from uuid import uuid4 as uuid
from typing import Union


class Cache:
    """creates redis instance"""
    def __init__(self):
        """stores the redis instance in the redis variable"""
        self._redis = redis.Redis()
        self._redis.flushdb()

    def store(self, data: Union[str, bytes, int, float]) -> str:
        """sets the key and data to the redis instance"""
        key = str(uuid())
        self._redis.set(key, data)
        return key
