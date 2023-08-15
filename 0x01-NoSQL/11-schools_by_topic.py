#!/usr/bin/env python3
'''11-schools_by_topic'''


def schools_by_topic(mongo_collection, topic):
    '''filters schools by topics offered'''
    return mongo_collection.find({'topics': topic})
