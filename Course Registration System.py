
# Course Registration System - Python Project

import time
from datetime import datetime

# ------------------ Databases ------------------

students_db = {
    "S001": {"name": "Ashim Shrestha", "courses": []},
    "S002": {"name": "Ram Shrestha", "courses": []},
    "S003": {"name": "Shyam Shrestha", "courses": []}
}

courses_db = {
    "C101": {"name": "Python Programming", "capacity": 3, "credits": 10},
    "C102": {"name": "Data Structures", "capacity": 2, "credits": 10},
    "C103": {"name": "Database Systems", "capacity": 2, "credits": 10},
    "C104": {"name": "Artificial Intelligence", "capacity": 2, "credits": 5}
}

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")

# ------------------ Login ------------------

def student_login():
    print("\n====== Course Registration System ======")
    sid = input("Enter Student ID: ")

    if sid in students_db:
        print(f"Welcome, {students_db[sid]['name']}")
        loading()
        return sid
    else:
        print("Invalid Student ID!")
        return None

# ------------------ Menu ------------------

def menu():
    print("\n========= MENU =========")
    print("1. View Courses")
    print("2. Register Course")
    print("3. Drop Course")
    print("4. My Courses")
    print("5. Exit")

# ------------------ Course List ------------------

def view_courses():
    print("\n====== Available Courses ======")
    for cid, c in courses_db.items():
        print(f"""
Course ID : {cid}
Name      : {c['name']}
Capacity  : {c['capacity']}
Credits   : {c['credits']}
---------------------------
""")

# ------------------ Register Course ------------------

def register_course(sid):
    view_courses()
    cid = input("Enter Course ID: ")

    if cid not in courses_db:
        print("Invalid Course ID!")
        return

    if cid in students_db[sid]["courses"]:
        print("Already registered in this course!")
        return

    if courses_db[cid]["capacity"] <= 0:
        print("Course is full!")
        return

    students_db[sid]["courses"].append(cid)
    courses_db[cid]["capacity"] -= 1

    loading()
    print("\n✅ Course Registered Successfully!")

# ------------------ Drop Course ------------------

def drop_course(sid):
    if not students_db[sid]["courses"]:
        print("No courses registered yet!")
        return

    print("\nYour Courses:")
    for cid in students_db[sid]["courses"]:
        print(f"{cid} - {courses_db[cid]['name']}")

    cid = input("\nEnter Course ID to Drop: ")

    if cid in students_db[sid]["courses"]:
        students_db[sid]["courses"].remove(cid)
        courses_db[cid]["capacity"] += 1
        loading()
        print("Course dropped successfully!")
    else:
        print("You are not registered in this course!")

# ------------------ My Courses ------------------

def my_courses(sid):
    print("\n====== My Registered Courses ======")
    if not students_db[sid]["courses"]:
        print("No courses registered.")
    else:
        total_credits = 0
        for cid in students_db[sid]["courses"]:
            c = courses_db[cid]
            total_credits += c['credits']
            print(f"{cid} - {c['name']} ({c['credits']} credits)")
        print(f"\nTotal Credits: {total_credits}")

# ------------------ Main System ------------------

def course_registration_system():
    while True:
        sid = student_login()
        if sid:
            while True:
                menu()
                ch = input("\nChoose Option (1-5): ")

                if ch == "1":
                    view_courses()
                elif ch == "2":
                    register_course(sid)
                elif ch == "3":
                    drop_course(sid)
                elif ch == "4":
                    my_courses(sid)
                elif ch == "5":
                    print("\nThank you for using Course Registration System!")
                    time.sleep(1)
                    break
                else:
                    print("Invalid Option!")

                input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
course_registration_system()
