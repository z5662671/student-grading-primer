from flask import Flask, jsonify, request
from flask_cors import CORS

import db

app = Flask(__name__)
CORS(app)

# Instructions:
# - Use the functions in backend/db.py in your implementation.
# - You are free to use additional data structures in your solution
# - You must define and tell your tutor one edge case you have devised and how you have addressed this

@app.route("/students")
def get_students():
    """
    Route to fetch all students from the database
    return: Array of student objects
    """
    
    return jsonify(db.get_all_students()), 200


@app.route("/students", methods=["POST"])
def create_student():
    """
    Route to create a new student
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The created student if successful
    """

    student_data = request.json
    
    name = student_data.get("name", None)
    course = student_data.get("course", None)
    mark = student_data.get("mark", None)

    if (name != None and course != None and mark != None):
        return jsonify(db.insert_student(name, course, mark)), 200
    else:
        return "Failed to create student", 404
    

@app.route("/students/<int:student_id>", methods=["PUT"])
def update_student(student_id):
    """
    Route to update student details by id
    param name: The name of the student (from request body)
    param course: The course the student is enrolled in (from request body)
    param mark: The mark the student received (from request body)
    return: The updated student if successful
    """
    
    student_data = request.json

    name = student_data.get("name", None)
    course = student_data.get("course", None)
    mark = student_data.get("mark", None)

    update_result = db.update_student(student_id, name, course, mark)

    if update_result != None:
        return jsonify(update_result), 200
    
    return "Failed to update student", 404


@app.route("/students/<int:student_id>", methods=["DELETE"])
def delete_student(student_id):
    """
    Route to delete student by id
    return: The deleted student
    """

    delete_result = db.delete_student(student_id)

    if delete_result != None:
        return jsonify(delete_result), 200

    return "Failed to delete student", 404


@app.route("/stats")
def get_stats():
    """
    Route to show the stats of all student marks 
    return: An object with the stats (count, average, min, max)
    """
    
    students = db.get_all_students()
    
    if (len(students) == 0):
        return "Failed to get stats", 404

    count = 0
    min = -1
    max = -1

    for student in students:
        count += student["mark"]

        if student["mark"] < min or min == -1:
            min = student["mark"]
        
        if student["mark"] > max or max == -1:
            max = student["mark"]
    
    return jsonify({"count": count, "average": count / len(students), "min": min, "max": max}), 200


@app.route("/")
def health():
    """Health check."""
    return {"status": "ok"}


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
