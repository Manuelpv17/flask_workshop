from flask import render_template, Blueprint, request, jsonify
from models.student_model import students

controller = Blueprint("controller", __name__)


@controller.route("/")
def hello_world():
    print(request.method)
    print(request.url)
    print(request.headers)
    print(request.json)
    # myResponse = Response(status=220, response="Hi",
    #   headers={"myheader": "hello"})
    return "<h1>Hello {}</h1>".format(students[0]["name"]), 220, {"myheader": "hello"}


@ controller.route("/students")
def students_templete():
    return render_template("students.html", students=students)


@ controller.route("/number/<string:id>")
def num(id):
    return id


@ controller.route("/api/students", methods=["GET", "POST"], strict_slashes=False)
def students_constroller():
    if request.method == "GET":
        return jsonify(students)
    elif request.method == "POST":
        students.append(request.json)
        return jsonify(students)


@ controller.route("/api/students/<int:id>", methods=["GET", "DELETE", "PUT"])
def student_controller(id):
    if request.method == "GET":
        for student in students:
            if student["id"] == id:
                return student
    elif request.method == "DELETE":
        for i in range(len(students)):
            if students[i]["id"] == id:
                students.pop(i)
        return jsonify(students)
    elif request.method == "PUT":
        for i in range(len(students)):
            if students[i]["id"] == id:
                students[i] = request.json
        return jsonify(students)
