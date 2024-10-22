#!/usr/bin/env python3
"""101 students"""
from pymongo import MongoClient


def top_students(mongo_collection):
    """Returns all students sorted by average score"""
    students = mongo_collection.find()
    result = []

    for student in students:
        total_score = sum(topic['score'] for topic in student.get('topics', []))
        average_score = total_score / len(student['topics']) if student['topics'] else 0
        student['averageScore'] = average_score
        result.append(student)

    # Sort the result by average score in descending order
    result.sort(key=lambda x: x['averageScore'], reverse=True)

    return result
