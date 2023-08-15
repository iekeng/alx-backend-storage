#!/usr/bin/env python3
'''12-log_stats'''
from pymongo import MongoClient


def log_stats(collection):
    document_count = collection.count_documents({})
    print(f"{document_count} logs")

    # Count methods
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print("Methods:")

    for method in methods:
        method_count = collection.count_documents({"method": method})
        print(f"\t{method}: {method_count}")

    status_count = collection.count_documents({"path": "/status"})
    print(f"{status_count} status check")


if __name__ == '__main__':
    collection = MongoClient().logs.nginx
    log_stats(collection)
