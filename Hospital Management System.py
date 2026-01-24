import datetime

# -------------------- Classes --------------------

class Patient:
    def __init__(self, pid, name, age, gender, disease):
        self.pid = pid
        self.name = name
        self.age = age
        self.gender = gender
        self.disease = disease

    def __str__(self):
        return f"{self.pid},{self.name},{self.age},{self.gender},{self.disease}"


class Doctor:
    def __init__(self, did, name, specialization):
        self.did = did
        self.name = name
        self.specialization = specialization

    def __str__(self):
        return f"{self.did},{self.name},{self.specialization}"


class Appointment:
    def __init__(self, pid, did, date):
        self.pid = pid
        self.did = did
        self.date = date

    def __str__(self):
        return f"{self.pid},{self.did},{self.date}"


# -------------------- Functions --------------------

def add_patient():
    pid = input("Patient ID: ")
    name = input("Name: ")
    age = input("Age: ")
    gender = input("Gender: ")
    disease = input("Disease: ")

    patient = Patient(pid, name, age, gender, disease)
    with open("patients.txt", "a") as f:
        f.write(str(patient) + "\n")

    print("Patient registered successfully.")


def view_patients():
    print("\n--- Patient Records ---")
    try:
        with open("patients.txt", "r") as f:
            for line in f:
                pid, name, age, gender, disease = line.strip().split(",")
                print(f"ID: {pid}, Name: {name}, Age: {age}, Gender: {gender}, Disease: {disease}")
    except FileNotFoundError:
        print("No patient records found.")


def add_doctor():
    did = input("Doctor ID: ")
    name = input("Name: ")
    specialization = input("Specialization: ")

    doctor = Doctor(did, name, specialization)
    with open("doctors.txt", "a") as f:
        f.write(str(doctor) + "\n")

    print("Doctor added successfully.")


def view_doctors():
    print("\n--- Doctor Records ---")
    try:
        with open("doctors.txt", "r") as f:
            for line in f:
                did, name, specialization = line.strip().split(",")
                print(f"ID: {did}, Name: {name}, Specialization: {specialization}")
    except FileNotFoundError:
        print("No doctor records found.")


def book_appointment():
    pid = input("Patient ID: ")
    did = input("Doctor ID: ")
    date = datetime.date.today()

    appointment = Appointment(pid, did, date)
    with open("appointments.txt", "a") as f:
        f.write(str(appointment) + "\n")

    print("Appointment booked successfully.")


def generate_bill():
    pid = input("Patient ID: ")
    amount = input("Total Amount: ")

    with open("bills.txt", "a") as f:
        f.write(f"{pid},{amount}\n")

    print("Bill generated successfully.")


# -------------------- Main Menu --------------------

def main():
    while True:
        print("\n===== Hospital Management System =====")
        print("1. Register Patient")
        print("2. View Patients")
        print("3. Add Doctor")
        print("4. View Doctors")
        print("5. Book Appointment")
        print("6. Generate Bill")
        print("7. Exit")

        choice = input("Enter choice: ")

        if choice == "1":
            add_patient()
        elif choice == "2":
            view_patients()
        elif choice == "3":
            add_doctor()
        elif choice == "4":
            view_doctors()
        elif choice == "5":
            book_appointment()
        elif choice == "6":
            generate_bill()
        elif choice == "7":
            print("Thank you for using HMS.")
            break
        else:
            print("Invalid choice. Try again.")


if __name__ == "__main__":
    main()