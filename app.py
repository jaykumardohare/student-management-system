from flask import Flask, render_template, request, redirect, session
import json, os

app = Flask(__name__)
app.secret_key = "secret123"

FILE = "students.json"

# Dummy user (for project)
USER = {"username": "jay", "password": "12345678"}

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

# Grade
def get_grade(p):
    if p >= 90: return "A"
    elif p >= 75: return "B"
    elif p >= 50: return "C"
    else: return "Fail"

# 🔒 LOGIN REQUIRED DECORATOR
def is_logged_in():
    return "user" in session

# LOGIN PAGE
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        u = request.form["username"]
        p = request.form["password"]

        if u == USER["username"] and p == USER["password"]:
            session["user"] = u
            return redirect("/")
        else:
            return "Invalid Credentials"

    return render_template("login.html")

# LOGOUT
@app.route("/logout")
def logout():
    session.pop("user", None)
    return redirect("/login")

# HOME (PROTECTED)
@app.route("/")
def home():
    if not is_logged_in():
        return redirect("/login")
    data = load_data()
    return render_template("index.html", students=data)

# ADD
@app.route("/add", methods=["POST"])
def add():
    if not is_logged_in():
        return redirect("/login")

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

# DELETE
@app.route("/delete/<roll>")
def delete(roll):
    if not is_logged_in():
        return redirect("/login")

    data = load_data()
    data = [s for s in data if s["roll"] != roll]
    save_data(data)
    return redirect("/")

# EDIT
@app.route("/edit/<roll>")
def edit(roll):
    if not is_logged_in():
        return redirect("/login")

    data = load_data()
    for s in data:
        if s["roll"] == roll:
            return render_template("edit.html", student=s)

# UPDATE
@app.route("/update/<roll>", methods=["POST"])
def update(roll):
    if not is_logged_in():
        return redirect("/login")

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

# PROFILE
@app.route("/profile/<roll>")
def profile(roll):
    if not is_logged_in():
        return redirect("/login")

    data = load_data()
    for s in data:
        if s["roll"] == roll:
            return render_template("profile.html", student=s)

if __name__ == "__main__":
    app.run(debug=True)