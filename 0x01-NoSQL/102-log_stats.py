#!/usr/bin/env python3
"""102 log stats"""
from pymongo import MongoClient


if __name__ == "__main__":
    """ Provides some stats about Nginx logs stored in MongoDB """
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    status_check = nginx_collection.count_documents(
        {"method": "GET", "path": "/status"}
    )
    print(f'{status_check} status check')

    # Count occurrences of each IP address
    ip_counts = {}
    for log in nginx_collection.find():
        ip = log.get('ip')
        if ip:
            ip_counts[ip] = ip_counts.get(ip, 0) + 1

    # Sort IPs by count in descending order and get the top 10
    sorted_ips = sorted(ip_counts.items(), key=lambda x: x[1], reverse=True)[:10]

    print('IPs:')
    for ip, count in sorted_ips:
        print(f'\t{ip}: {count}')
