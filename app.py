from flask import Flask, render_template, request, redirect
import json, os

app = Flask(__name__)
FILE = "students.json"

if not os.path.exists(FILE):
    with open(FILE, "w") as f:
        json.dump([], f)

def load_data():
    with open(FILE, "r") as f:
        return json.load(f)

def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Grade function
def get_grade(marks):
    if marks >= 90:
        return "A"
    elif marks >= 75:
        return "B"
    elif marks >= 50:
        return "C"
    else:
        return "Fail"

@app.route("/")
def index():
    students = load_data()
    search = request.args.get("search")

    if search:
        students = [s for s in students if search.lower() in s["name"].lower() or search in s["roll"]]

    return render_template("index.html", students=students)

@app.route("/add", methods=["POST"])
def add():
    data = load_data()

    name = request.form["name"]
    roll = request.form["roll"]
    marks = int(request.form["marks"])

    student = {
        "name": name,
        "roll": roll,
        "marks": marks,
        "percentage": marks,
        "grade": get_grade(marks)
    }

    data.append(student)
    save_data(data)
    return redirect("/")

@app.route("/delete/<roll>")
def delete(roll):
    data = load_data()
    data = [s for s in data if s["roll"] != roll]
    save_data(data)
    return redirect("/")

@app.route("/edit/<roll>")
def edit(roll):
    data = load_data()
    for s in data:
        if s["roll"] == roll:
            return render_template("edit.html", student=s)

@app.route("/update/<roll>", methods=["POST"])
def update(roll):
    data = load_data()
    for s in data:
        if s["roll"] == roll:
            s["name"] = request.form["name"]
            s["marks"] = int(request.form["marks"])
            s["percentage"] = s["marks"]
            s["grade"] = get_grade(s["marks"])
            break

    save_data(data)
    return redirect("/")

if __name__ == "__main__":
    app.run(debug=True)