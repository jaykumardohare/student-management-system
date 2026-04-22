# 🎓 Student Management System (Flask Based)

## 📌 Project Overview

The Student Management System is a web-based application developed using Python and Flask framework.
It allows users to manage student records efficiently with a modern user interface.

This system includes features like adding students, updating details, deleting records, viewing profiles, and managing multi-subject marks.

---

## 🚀 Features

* 🔐 Login & Logout Authentication System
* ➕ Add Student with Full Details
* ✏️ Update Student Information
* ❌ Delete Student Record
* 👤 View Student Profile (Separate Page)
* 📚 Multi-Subject Marks System
* 📊 Automatic Total, Percentage & Grade Calculation
* 🎨 Modern UI using Bootstrap
* 💾 Data stored in JSON file

---

## 🧠 Technologies Used

* Python
* Flask
* HTML
* CSS (Bootstrap)
* JSON

---

## 📁 Project Structure

```
student_web_project/
│
├── app.py
├── students.json
│
└── templates/
    ├── index.html
    ├── edit.html
    ├── profile.html
    └── login.html
```

---

## ▶️ How to Run the Project

1. Install Python (3.x)

2. Install Flask:

   ```bash
   pip install flask
   ```

3. Run the application:

   ```bash
   python app.py
   ```

4. Open browser:

   ```
   http://127.0.0.1:5000
   ```

---

## 🔐 Login Credentials

* Username: `admin`
* Password: `1234`

---

## 📊 Student Data Format

Each student record is stored in JSON format:

```json
{
  "name": "Jay",
  "roll": "101",
  "enroll": "2025A01",
  "dob": "2005-01-01",
  "subjects": {
    "Math": 80,
    "Science": 75,
    "English": 85
  },
  "total": 240,
  "percentage": 80,
  "grade": "A"
}
```

---

## 🌐 Deployment

The project can be deployed on platforms like Render.

Steps:

* Push code to GitHub
* Connect GitHub repo to Render
* Enable auto deploy
* Deploy latest commit

---

## 🚀 Future Scope

* Database integration (MySQL / MongoDB)
* User roles (Admin / Student)
* PDF Report Generation
* Graphs & Analytics
* Mobile Application

---

## 👨‍💻 Author

**Jay Kumar Dohare**

---

## ⭐ Conclusion

This project demonstrates a complete web-based student management system using Flask.
It provides practical understanding of CRUD operations, authentication, and UI design.

---

✨ *This is a complete A1-level academic project with real-world features.*
