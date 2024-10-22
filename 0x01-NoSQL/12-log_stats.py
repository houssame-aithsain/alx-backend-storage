#!/usr/bin/env python3
""" 12-log_stats """


from pymongo import MongoClient


def main():
    """Provides statistics about Nginx logs stored in MongoDB."""
    client = MongoClient('mongodb://127.0.0.1:27017')
    nginx_collection = client.logs.nginx

    # Count total logs
    n_logs = nginx_collection.count_documents({})
    print(f'{n_logs} logs')

    # Define HTTP methods to count
    methods = ["GET", "POST", "PUT", "PATCH", "DELETE"]
    print('Methods:')
    
    # Count and display occurrences for each method
    for method in methods:
        count = nginx_collection.count_documents({"method": method})
        print(f'\tmethod {method}: {count}')

    # Count and display status checks
    status_check = nginx_collection.count_documents({"method": "GET", "path": "/status"})
    print(f'{status_check} status check')

if __name__ == "__main__":
    main()
