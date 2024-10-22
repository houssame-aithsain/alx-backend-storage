#!/usr/bin/env python3
""" 8-all """


def list_all(mongo_collection):
    """Return a list of all documents in a collection."""
    return list(mongo_collection.find())
