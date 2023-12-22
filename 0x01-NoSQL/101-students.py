#!/usr/bin/env python3
"""This script contains a function that returns
all students sorted by average score
"""


def myFunc(s):
    """This function returns the average
    score of the student dictionary passed
    as argument
    """
    return s["averageScore"]


def top_students(mongo_collection):
    """This function returns all students
    sorted by their average score
    """
    new_students = []

    # Get all students
    students = mongo_collection.find()

    # Iterate over each student
    for s in students:
        topics = s.get("topics")
        sum = 0
        n = 0

        # Loop over each topic, find the average and
        # update the student's document with ave score
        for t in topics:
            sum = sum + float(t.get("score"))
            n += 1
        mongo_collection.update_one({"name": s.get("name")},
                                    {"$set": {"averageScore": sum / n}})

        # Append the student into the list
        new_students.append(mongo_collection.find({"name": s.get("name")})[0])

    new_students.sort(reverse=True, key=myFunc)
    return new_students
