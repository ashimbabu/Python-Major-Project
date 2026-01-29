from employee import Employee
from database import load_data, save_data
from auth import login

def add_employee():
    print("\n--- Add New Employee ---")
    emp_id = input("Employee ID: ")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    department = input("Department: ")
    position = input("Position: ")
    salary = input("Salary: ")
    email = input("Email: ")
    phone = input("Phone: ")

    emp = Employee(emp_id, name, age, gender, department, position, salary, email, phone)
    data = load_data()
    data.append(emp.to_dict())
    save_data(data)
    print("Employee added successfully!")

def view_employees():
    print("\n--- Employee List ---")
    data = load_data()
    if not data:
        print("No employees found.")
        return
    for emp in data:
        print("="*40)
        for k,v in emp.items():
            print(f"{k.capitalize()}: {v}")

def search_employee():
    emp_id = input("\nEnter Employee ID to search: ")
    data = load_data()
    for emp in data:
        if emp["emp_id"] == emp_id:
            print("\nEmployee Found:")
            for k,v in emp.items():
                print(f"{k.capitalize()}: {v}")
            return
    print("Employee not found.")

def update_employee():
    emp_id = input("\nEnter Employee ID to update: ")
    data = load_data()
    for emp in data:
        if emp["emp_id"] == emp_id:
            print("Leave blank to keep old value.")
            emp["name"] = input("Name: ") or emp["name"]
            emp["age"] = input("Age: ") or emp["age"]
            emp["department"] = input("Department: ") or emp["department"]
            emp["position"] = input("Position: ") or emp["position"]
            emp["salary"] = input("Salary: ") or emp["salary"]
            save_data(data)
            print("Employee updated successfully!")
            return
    print("Employee not found.")

def delete_employee():
    emp_id = input("\nEnter Employee ID to delete: ")
    data = load_data()
    new_data = [emp for emp in data if emp["emp_id"] != emp_id]
    if len(new_data) == len(data):
        print("Employee not found.")
    else:
        save_data(new_data)
        print("Employee deleted successfully!")

def menu():
    print("""
========== Employee Management System ==========
1. Add Employee
2. View Employees
3. Search Employee
4. Update Employee
5. Delete Employee
6. Exit
===============================================
""")

def main():
    if not login():
        return

    while True:
        menu()
        choice = input("Enter choice: ")

        if choice == "1":
            add_employee()
        elif choice == "2":
            view_employees()
        elif choice == "3":
            search_employee()
        elif choice == "4":
            update_employee()
        elif choice == "5":
            delete_employee()
        elif choice == "6":
            print("Exiting system...")
            break
        else:
            print("Invalid choice!")

if __name__ == "__main__":
    main()