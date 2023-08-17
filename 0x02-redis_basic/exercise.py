#!/usr/bin/env python3
"""Redis db"""
import redis
from uuid import uuid4 as uuid
from typing import Union, Callable


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

    def get(self, key: str,
            fn: Callable = None) -> Union[str, bytes, int, float]:
        '''get method'''
        data = self._redis.get(key)
        if data is None:
            return None
        elif fn:
            return fn(data)
        return data

    def get_str(self, key: str) -> str:
        '''returns a srting when called'''
        data = self_redis.get(key)
        return str(data)

    def get_int(self, key: str) -> int:
        '''returns an int when called'''
        data = self_redis.get(key)
        return int(data)
