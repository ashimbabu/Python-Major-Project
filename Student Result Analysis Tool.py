# ============================================
# Student Result Analysis Tool - Python Project
# ============================================

import json
import time
from datetime import datetime

DB_FILE = "students_db.json"

# ------------------ Database ------------------

def load_data():
    try:
        with open(DB_FILE, "r") as f:
            return json.load(f)
    except:
        return []


def save_data(data):
    with open(DB_FILE, "w") as f:
        json.dump(data, f, indent=4)

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.3)
        print(".", end="")
    print("\n")

# ------------------ Menu ------------------

def menu():
    print("\n========= STUDENT RESULT ANALYSIS SYSTEM =========")
    print("1. Add Student Result")
    print("2. View All Results")
    print("3. Student-wise Report")
    print("4. Subject-wise Analysis")
    print("5. Class Performance Report")
    print("6. Topper List")
    print("7. Delete Student Record")
    print("8. Exit")

# ------------------ Add Student ------------------

def add_student(data):
    try:
        sid = input("Student ID: ")
        name = input("Student Name: ")
        cls = input("Class: ")
        subjects = {}

        print("Enter Marks (out of 100):")
        for sub in ["Math", "Science", "English", "Computer", "Social"]:
            subjects[sub] = float(input(f"{sub}: "))

        total = sum(subjects.values())
        percentage = total / len(subjects)

        if percentage >= 80:
            grade = "A"
        elif percentage >= 60:
            grade = "B"
        elif percentage >= 40:
            grade = "C"
        else:
            grade = "Fail"

        record = {
            "id": sid,
            "name": name,
            "class": cls,
            "subjects": subjects,
            "total": total,
            "percentage": round(percentage, 2),
            "grade": grade,
            "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data.append(record)
        save_data(data)
        loading()
        print("\n✅ Student Result Added Successfully!")
    except:
        print("Invalid Input!")

# ------------------ View Results ------------------

def view_results(data):
    print("\n====== All Student Results ======")
    if not data:
        print("No records found.")
        return

    for i, s in enumerate(data, 1):
        print(f"{i}. {s['id']} | {s['name']} | Class {s['class']} | {s['percentage']}% | Grade: {s['grade']}")

# ------------------ Student-wise Report ------------------

def student_report(data):
    sid = input("\nEnter Student ID: ")
    found = False

    for s in data:
        if s['id'] == sid:
            print("\n====== Student Report ======")
            print(f"Name       : {s['name']}")
            print(f"Class      : {s['class']}")
            print(f"Total      : {s['total']}")
            print(f"Percentage : {s['percentage']}%")
            print(f"Grade      : {s['grade']}")
            print("Subjects:")
            for sub, m in s['subjects'].items():
                print(f"  {sub} : {m}")
            found = True

    if not found:
        print("Student not found!")

# ------------------ Subject-wise Analysis ------------------

def subject_analysis(data):
    print("\n====== Subject-wise Analysis ======")
    subjects = {"Math": [], "Science": [], "English": [], "Computer": [], "Social": []}

    for s in data:
        for sub in subjects:
            subjects[sub].append(s['subjects'][sub])

    for sub, marks in subjects.items():
        if marks:
            avg = sum(marks)/len(marks)
            print(f"{sub} -> Avg: {round(avg,2)} | Max: {max(marks)} | Min: {min(marks)}")

# ------------------ Class Performance ------------------

def class_performance(data):
    print("\n====== Class Performance Report ======")
    classes = {}

    for s in data:
        classes.setdefault(s['class'], []).append(s['percentage'])

    for cls, percs in classes.items():
        avg = sum(percs)/len(percs)
        print(f"Class {cls} -> Avg Performance: {round(avg,2)}% | Students: {len(percs)}")

# ------------------ Topper List ------------------

def topper_list(data):
    print("\n====== Topper List ======")
    if not data:
        print("No records available.")
        return

    sorted_data = sorted(data, key=lambda x: x['percentage'], reverse=True)

    for i, s in enumerate(sorted_data[:5], 1):
        print(f"{i}. {s['name']} | Class {s['class']} | {s['percentage']}% | Grade {s['grade']}")

# ------------------ Delete Record ------------------

def delete_record(data):
    view_results(data)
    if not data:
        return

    try:
        idx = int(input("\nEnter Record Number to Delete: "))
        if 1 <= idx <= len(data):
            data.pop(idx-1)
            save_data(data)
            loading()
            print("\n✅ Record Deleted Successfully!")
        else:
            print("Invalid Number!")
    except:
        print("Invalid Input!")

# ------------------ Main System ------------------

def result_system():
    data = load_data()

    while True:
        menu()
        ch = input("\nChoose Option (1-8): ")

        if ch == "1":
            add_student(data)
        elif ch == "2":
            view_results(data)
        elif ch == "3":
            student_report(data)
        elif ch == "4":
            subject_analysis(data)
        elif ch == "5":
            class_performance(data)
        elif ch == "6":
            topper_list(data)
        elif ch == "7":
            delete_record(data)
        elif ch == "8":
            print("\nExiting Student Result Analysis Tool...")
            time.sleep(1)
            break
        else:
            print("Invalid Option!")

        input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
result_system()
