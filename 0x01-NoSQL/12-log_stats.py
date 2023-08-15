#!/usr/bin/env python3
'''12-log_stats'''
from pymongo import MongoClient


client = MongoClient()
db = client['logs']
nginx = db['nginx']

document_count = nginx.count_documents({})
get_count = nginx.count_documents({"method": "GET"})
post_count = nginx.count_documents({"method": "POST"})
put_count = nginx.count_documents({"method": "PUT"})
patch_count = nginx.count_documents({"method": "PATCH"})
delete_count = nginx.count_documents({"method": "DELETE"})
status_count = nginx.count_documents({"path": "/status"})

print(f"{document_count} logs\nMethods:\n\tmethod GET: {get_count}\
\n\tmethod POST: {post_count}\n\tmethod PUT: {put_count}\
\n\tmethod PATCH: {patch_count}\n\tmethod DELETE: {delete_count}\n\
{status_count} status check")
