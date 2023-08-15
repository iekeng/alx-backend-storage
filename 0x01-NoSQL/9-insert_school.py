#!/usr/bin/env python3
'''inserts new data into collection'''


def insert_school(mongo_collection, **kwargs):
    '''returns document id'''
    document = mongo_collection.insert_one(kwargs)
    return document.inserted_id

