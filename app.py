from flask import Flask, render_template, request, redirect
import json
import os

app = Flask(__name__)

FILE = "students.json"

# Load data
def load_data():
    if not os.path.exists(FILE):
        return []
    with open(FILE, "r") as f:
        return json.load(f)

# Save data
def save_data(data):
    with open(FILE, "w") as f:
        json.dump(data, f, indent=4)

# Grade function
def get_grade(p):
    if p >= 90:
        return "A"
    elif p >= 75:
        return "B"
    elif p >= 50:
        return "C"
    else:
        return "Fail"

# Home
@app.route("/")
def home():
    data = load_data()
    return render_template("index.html", students=data)

# Add student
@app.route("/add", methods=["POST"])
def add():
    data = load_data()

    name = request.form["name"]
    roll = request.form["roll"]
    enroll = request.form["enroll"]
    dob = request.form["dob"]

    math = int(request.form["math"])
    science = int(request.form["science"])
    english = int(request.form["english"])

    total = math + science + english
    percentage = round(total / 3, 2)

    student = {
        "name": name,
        "roll": roll,
        "enroll": enroll,
        "dob": dob,
        "subjects": {
            "Math": math,
            "Science": science,
            "English": english
        },
        "total": total,
        "percentage": percentage,
        "grade": get_grade(percentage)
    }

    data.append(student)
    save_data(data)
    return redirect("/")

# Delete
@app.route("/delete/<roll>")
def delete(roll):
    data = load_data()
    data = [s for s in data if s["roll"] != roll]
    save_data(data)
    return redirect("/")

# Edit page
@app.route("/edit/<roll>")
def edit(roll):
    data = load_data()
    for s in data:
        if s["roll"] == roll:
            return render_template("edit.html", student=s)

# Update
@app.route("/update/<roll>", methods=["POST"])
def update(roll):
    data = load_data()

    for s in data:
        if s["roll"] == roll:
            s["name"] = request.form["name"]
            s["enroll"] = request.form["enroll"]
            s["dob"] = request.form["dob"]

            math = int(request.form["math"])
            science = int(request.form["science"])
            english = int(request.form["english"])

            total = math + science + english
            percentage = round(total / 3, 2)

            s["subjects"] = {
                "Math": math,
                "Science": science,
                "English": english
            }
            s["total"] = total
            s["percentage"] = percentage
            s["grade"] = get_grade(percentage)

    save_data(data)
    return redirect("/")

# Profile page
@app.route("/profile/<roll>")
def profile(roll):
    data = load_data()
    for s in data:
        if s["roll"] == roll:
            return render_template("profile.html", student=s)

if __name__ == "__main__":
    app.run(debug=True)