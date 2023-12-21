#!/usr/bin/env python3
"""This script contains a function that retreives
all documents from a collection
"""


def list_all(mongo_collection):
    """This function retrieves all documents from
    a collection
    """
    results = mongo_collection.find()
    return results
