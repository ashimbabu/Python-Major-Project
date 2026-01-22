import json
import os

FILE_NAME = "students.json"

# ---------------- File Handling ----------------
def load_students():
    if not os.path.exists(FILE_NAME):
        return {}
    with open(FILE_NAME, "r") as file:
        return json.load(file)

def save_students(students):
    with open(FILE_NAME, "w") as file:
        json.dump(students, file, indent=4)

# ---------------- Core Functions ----------------
def add_student():
    students = load_students()
    student_id = input("Enter Student ID: ")

    if student_id in students:
        print("Student ID already exists!")
        return

    name = input("Enter Name: ")
    age = input("Enter Age: ")
    course = input("Enter Course: ")
    contact = input("Enter Contact Number: ")

    students[student_id] = {
        "Name": name,
        "Age": age,
        "Course": course,
        "Contact": contact
    }

    save_students(students)
    print("Student added successfully!")

def view_students():
    students = load_students()
    if not students:
        print("No student records found.")
        return

    print("\n--- Student Records ---")
    for sid, details in students.items():
        print(f"\nID: {sid}")
        for key, value in details.items():
            print(f"{key}: {value}")

def search_student():
    students = load_students()
    student_id = input("Enter Student ID to search: ")

    if student_id in students:
        print("\nStudent Found:")
        for key, value in students[student_id].items():
            print(f"{key}: {value}")
    else:
        print("Student not found!")

def update_student():
    students = load_students()
    student_id = input("Enter Student ID to update: ")

    if student_id not in students:
        print("Student not found!")
        return

    print("Leave blank to keep existing value.")
    name = input("New Name: ")
    age = input("New Age: ")
    course = input("New Course: ")
    contact = input("New Contact: ")

    if name:
        students[student_id]["Name"] = name
    if age:
        students[student_id]["Age"] = age
    if course:
        students[student_id]["Course"] = course
    if contact:
        students[student_id]["Contact"] = contact

    save_students(students)
    print("Student updated successfully!")

def delete_student():
    students = load_students()
    student_id = input("Enter Student ID to delete: ")

    if student_id in students:
        del students[student_id]
        save_students(students)
        print("Student deleted successfully!")
    else:
        print("Student not found!")

# ---------------- Main Menu ----------------
def main():
    while True:
        print("\n===== Student Information Management System =====")
        print("1. Add Student")
        print("2. View All Students")
        print("3. Search Student")
        print("4. Update Student")
        print("5. Delete Student")
        print("6. Exit")

        choice = input("Enter your choice (1-6): ")

        if choice == "1":
            add_student()
        elif choice == "2":
            view_students()
        elif choice == "3":
            search_student()
        elif choice == "4":
            update_student()
        elif choice == "5":
            delete_student()
        elif choice == "6":
            print("Exiting system. Goodbye!")
            break
        else:
            print("Invalid choice! Try again.")

# ---------------- Run Program ----------------
if __name__ == "__main__":
    main()
