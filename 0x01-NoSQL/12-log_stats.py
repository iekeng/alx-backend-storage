#!/usr/bin/env python3
'''12-log_stats'''
from pymongo import MongoClient


client = MongoClient()
db = client['logs']
nginx = db['nginx']

document_count = nginx.count_documents({})
print(f"{document_count} logs")

# Count methods
methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")

for method in methods:
        method_count = nginx.count_documents({"method": method})
        print(f"\t{method}: {method_count}")

status_count = nginx.count_documents({"path": "/status"})
print(f"{status_count} status check")

