#!/usr/bin/env python3
"""This script provides some stats about nginx
logs stored in MongoDB
"""

from pymongo import MongoClient
from typing import List


# Create a connection to the mongodb database and select the nginx collection
client = MongoClient()
db = client.logs
nginx_collection = db.nginx

# Count and print the total number of documents in the nginx collection
num_nginx_logs: int = len(list(nginx_collection.find()))
print(f"{num_nginx_logs} logs")

# Count and print all the documents with all the different http methods
methods: List[str] = ["GET", "POST", "PUT", "PATCH", "DELETE"]
print("Methods:")
for m in methods:
    total_num_method = len(list(nginx_collection.find({"method": m})))
    print(f"    method {m}: {total_num_method}")

# Count and print the number of GET requests that were status checks
num_status_check: int = len(list(
    nginx_collection.find({"method": "GET", "path": "/status"})))
print(f"{num_status_check} status check")

# Close the connection afterwards
client.close
