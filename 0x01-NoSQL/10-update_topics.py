#!/usr/bin/env python3
'''10-update_topics'''


def update_topics(mongo_collection, name, topics):
    """changes all topics"""
    fil = {"name": name}
    new_vals = {"$set": {"topics": topics}}
    mongo_collection.update_many(fil, new_vals)
