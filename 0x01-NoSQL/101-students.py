#!/usr/bin/env python3
'''101-students'''


def top_students(mongo_collection):
    '''Returns average score of students in a collection and ranks them'''
    return mongo_collection.aggregate([{
        "$project": {
            "name": "$name",
            "averageScore": {"$avg": "$topics.score"}
            }
        }, {"$sort": {"averageScore": -1}}])
