#!/usr/bin/env python3
"""
Provide some stats about Nginx logs stored in MongoDB
Database: logs, Collection: nginx, Display same as example
first line: x logs, x number of documents in this collection
second line: Methods
5 lines with method = ["GET", "POST", "PUT", "PATCH", "DELETE"]
one line with method=GET, path=/status
"""
from pymongo import MongoClient


METHODS = ["GET", "POST", "PUT", "PATCH", "DELETE"]


def log_stats(mongo_collection):
    """
    Prototype: def log_stats(mongo_collection, option=None):
    Provide some stats about Nginx logs stored in MongoDB
    """
    items = {}
    result = mongo_collection.count_documents(items)
    print(f"{result} logs")
    print("Methods:")

    method_counts = {}  # Dictionary to store method counts
    for method in METHODS:
        count = mongo_collection.count_documents({"method": method})
        method_counts[method] = count

    for method, count in method_counts.items():
        print(f"\tmethod {method}: {count}")

    status_check = mongo_collection.count_documents({"method": "GET",
                                                    "path": "/status"})
    print(f"{status_check} status check")

    print("IPs:")

    top_ips = mongo_collection.aggregate([
        {"$group": {
            "_id": "$ip",
            "count": {"$sum": 1}
        }
        },
        {"$sort": {"count": -1}},
        {"$limit": 10},
        {"$project": {
            "_id": 0,
            "ip": "$_id",
            "count": 1
        }}
    ])

    formatted_ips = ["\t{}: {}".format(top_ip.get("ip"),
                                       top_ip.get("count"))
                     for top_ip in top_ips]
    print("\n".join(formatted_ips))


if __name__ == "__main__":
    nginx_collection = MongoClient('mongodb://127.0.0.1:27017').logs.nginx
    log_stats(nginx_collection)
