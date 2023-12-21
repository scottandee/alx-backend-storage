#!/usr/bin/env python3
"""This script contains a function that
changes all topics of a school document
based on the name
"""


def update_topics(mongo_collection, name, topics):
    """This function changes all topics of a school
    document based on the name
    """
    mongo_collection.update_one({"name": name}, {"$set": {"topics": topics}})
