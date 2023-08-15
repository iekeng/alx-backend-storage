#!/usr/bin/env python3
'''lists all documents in a collection'''


def list_all(mongo_collection):
    '''returns an empty array if collection is none'''
    if mongo_collection is None:
        return []

    return mongo_collection.find()
