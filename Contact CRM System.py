
# Contact CRM System

import json
import time
from datetime import datetime

DB_FILE = "contacts_db.json"

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
    print("\n========= CONTACT CRM SYSTEM =========")
    print("1. Add Contact")
    print("2. View All Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. CRM Reports")
    print("7. Exit")

# ------------------ Add Contact ------------------

def add_contact(data):
    try:
        cid = input("Contact ID: ")
        name = input("Full Name: ")
        phone = input("Phone Number: ")
        email = input("Email: ")
        company = input("Company/Organization: ")
        category = input("Category (Client/Lead/Vendor/Personal): ")

        record = {
            "id": cid,
            "name": name,
            "phone": phone,
            "email": email,
            "company": company,
            "category": category,
            "created": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
        }

        data.append(record)
        save_data(data)
        loading()
        print("\n✅ Contact Added Successfully!")
    except:
        print("Invalid Input!")

# ------------------ View Contacts ------------------

def view_contacts(data):
    print("\n====== Contact List ======")
    if not data:
        print("No contacts found.")
        return

    for i, c in enumerate(data, 1):
        print(f"{i}. {c['id']} | {c['name']} | {c['phone']} | {c['email']} | {c['company']} | {c['category']}")

# ------------------ Search Contact ------------------

def search_contact(data):
    key = input("\nEnter Name/Phone/Email to Search: ").lower()
    found = False

    print("\n====== Search Results ======")
    for c in data:
        if key in c['name'].lower() or key in c['phone'] or key in c['email'].lower():
            print(f"{c['id']} | {c['name']} | {c['phone']} | {c['email']} | {c['company']} | {c['category']}")
            found = True

    if not found:
        print("No matching contact found.")

# ------------------ Update Contact ------------------

def update_contact(data):
    cid = input("\nEnter Contact ID to Update: ")

    for c in data:
        if c['id'] == cid:
            print("Leave field empty to keep old value")
            name = input(f"Name ({c['name']}): ") or c['name']
            phone = input(f"Phone ({c['phone']}): ") or c['phone']
            email = input(f"Email ({c['email']}): ") or c['email']
            company = input(f"Company ({c['company']}): ") or c['company']
            category = input(f"Category ({c['category']}): ") or c['category']

            c.update({
                "name": name,
                "phone": phone,
                "email": email,
                "company": company,
                "category": category,
                "updated": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
            })

            save_data(data)
            loading()
            print("\n✅ Contact Updated Successfully!")
            return

    print("Contact ID not found!")

# ------------------ Delete Contact ------------------

def delete_contact(data):
    view_contacts(data)
    if not data:
        return

    cid = input("\nEnter Contact ID to Delete: ")
    for i, c in enumerate(data):
        if c['id'] == cid:
            data.pop(i)
            save_data(data)
            loading()
            print("\n✅ Contact Deleted Successfully!")
            return

    print("Contact ID not found!")

# ------------------ CRM Reports ------------------

def crm_reports(data):
    print("\n====== CRM REPORTS ======")
    print("1. Category-wise Contacts")
    print("2. Company-wise Contacts")
    print("3. Total CRM Summary")

    ch = input("Choose Option: ")

    if ch == "1":
        report = {}
        for c in data:
            report[c['category']] = report.get(c['category'], 0) + 1
        print("\nCategory-wise Report:")
        for k, v in report.items():
            print(f"{k} : {v}")

    elif ch == "2":
        report = {}
        for c in data:
            report[c['company']] = report.get(c['company'], 0) + 1
        print("\nCompany-wise Report:")
        for k, v in report.items():
            print(f"{k} : {v}")

    elif ch == "3":
        print("\nTotal Contacts:", len(data))
        categories = set(c['category'] for c in data)
        companies = set(c['company'] for c in data)
        print("Total Categories:", len(categories))
        print("Total Companies:", len(companies))

    else:
        print("Invalid Option!")

# ------------------ Main System ------------------

def crm_system():
    data = load_data()

    while True:
        menu()
        ch = input("\nChoose Option (1-7): ")

        if ch == "1":
            add_contact(data)
        elif ch == "2":
            view_contacts(data)
        elif ch == "3":
            search_contact(data)
        elif ch == "4":
            update_contact(data)
        elif ch == "5":
            delete_contact(data)
        elif ch == "6":
            crm_reports(data)
        elif ch == "7":
            print("\nExiting Contact CRM System...")
            time.sleep(1)
            break
        else:
            print("Invalid Option!")

        input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
crm_system()
