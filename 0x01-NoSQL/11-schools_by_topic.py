#!/usr/bin/python3
"""This script contains a function that
returns a list of schools that have a specific
topic
"""

from typing import List


def schools_by_topic(mongo_collection, topic):
    """This function returns a list of schools
    that have a specific topic
    """
    result: List = []
    schools = mongo_collection.find()
    for sch in schools:
        if sch.get("topics"):
            if topic in sch.get("topics"):
                result.append(sch)
    return result
