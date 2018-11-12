from flask import Flask, render_template, jsonify, request
from student import Student
from sqlalchemy import text
import json

app = Flask(__name__)

#Initializing a base set of students for the API
students = [
    Student(1,"Arthur Coll",1,"DT228"),
    Student(2,"James Brock",2,"DT211"),
    Student(3,"Jason Black",3,"DT181")
]

def obj_dict(obj):
    return obj.__dict__


@app.route("/api/students", methods=['GET','POST'])
def list_students():
    if request.method == 'GET':
        json_string = json.dumps(students, default=obj_dict)
        return json_string, 200

    if request.method == 'POST':
        for student in students:
            if student.student_id == request.form['student_id']:
                return jsonify({"error": "Student ID Already exists"}), 409

        new = Student(
        student_id = request.form['student_id'],
        name = request.form['name'],
        year = request.form['year'],
        course = request.form['course']
        )

        students.append(new)
        return jsonify({"result": "Student added to database"}), 200



@app.route("/api/students/<int:student_id>", methods=['GET', 'PUT', 'DELETE'])
def api_student_id(student_id):

    if request.method == 'GET':
        for student in students:
            if student.student_id == student_id:
                return jsonify({
                        "student_id": student.student_id,
                        "name": student.name,
                        "year": student.year,
                        "course": student.course
                    })

        else:
            return jsonify({"error": "Invalid student_id"}), 404



    if request.method == 'PUT':
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                student = Student(
                student_id = request.form['student_id'],
                name = request.form['name'],
                year = request.form['year'],
                course = request.form['course']
                )
                students.append(student)

                return jsonify({"result": "Student details updated"}), 200


        return jsonify({"error": "Invalid student_id"}), 404



    if request.method == 'DELETE':
        for student in students:
            if student.student_id == student_id:
                students.remove(student)
                return jsonify({"result": "Student removed"}), 200
            else:
                return jsonify({"error": "Invalid student_id"}), 404
