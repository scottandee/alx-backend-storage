#!/usr/bin/env python3
"""This script contains a function that
inserts a new document into a collection
based of `kwargs`
"""


def insert_school(mongo_collection, **kwargs):
    """This script inserts a new document into
    a collection based on kwargs
    """
    result = mongo_collection.insert_one(kwargs)
    return result.inserted_id
