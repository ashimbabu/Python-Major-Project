
# Online Examination System


import time
import random
from datetime import datetime

# ------------------ Databases ------------------

users_db = {
    "ashim": {"password": "1234", "results": []},
    "student1": {"password": "1111", "results": []}
}

questions_db = {
    "Python": [
        {
            "q": "What is Python?",
            "options": ["Programming Language", "Snake", "Game", "OS"],
            "answer": "Programming Language"
        },
        {
            "q": "Which keyword is used to define a function?",
            "options": ["func", "define", "def", "function"],
            "answer": "def"
        },
        {
            "q": "Which data type is immutable?",
            "options": ["List", "Set", "Dictionary", "Tuple"],
            "answer": "Tuple"
        },
        {
            "q": "Which symbol is used for comments?",
            "options": ["//", "#", "/*", "**"],
            "answer": "#"
        }
    ],
    "General Knowledge": [
        {
            "q": "Capital of Nepal?",
            "options": ["Pokhara", "Biratnagar", "Kathmandu", "Lalitpur"],
            "answer": "Kathmandu"
        },
        {
            "q": "Largest planet?",
            "options": ["Earth", "Mars", "Jupiter", "Venus"],
            "answer": "Jupiter"
        }
    ]
}

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")

# ------------------ Login ------------------

def login():
    print("\n====== Online Examination System ======")
    user = input("Username: ")
    pwd = input("Password: ")

    if user in users_db and users_db[user]["password"] == pwd:
        print("Login Successful!")
        loading()
        return user
    else:
        print("Invalid Login!")
        return None

# ------------------ Menu ------------------

def menu():
    print("\n========= MAIN MENU =========")
    print("1. View Subjects")
    print("2. Start Exam")
    print("3. View Results")
    print("4. Exit")

# ------------------ Subjects ------------------

def view_subjects():
    print("\nAvailable Subjects:")
    for i, sub in enumerate(questions_db.keys(), 1):
        print(f"{i}. {sub}")

# ------------------ Exam Engine ------------------

def start_exam(user):
    view_subjects()
    subject = input("\nEnter Subject Name: ")

    if subject not in questions_db:
        print("Invalid Subject!")
        return

    questions = questions_db[subject]
    random.shuffle(questions)

    score = 0
    total = len(questions)

    print(f"\nExam Started: {subject}")
    print("===========================")

    for i, q in enumerate(questions, 1):
        print(f"\nQ{i}. {q['q']}")
        for idx, opt in enumerate(q['options'], 1):
            print(f"   {idx}. {opt}")

        try:
            ans = int(input("Your Answer (1-4): "))
            if q['options'][ans-1] == q['answer']:
                score += 1
        except:
            pass

    percent = (score / total) * 100

    result = {
        "subject": subject,
        "score": score,
        "total": total,
        "percentage": round(percent, 2),
        "date": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    users_db[user]["results"].append(result)

    loading()
    print("\n====== Exam Result ======")
    print(f"Subject    : {subject}")
    print(f"Score      : {score}/{total}")
    print(f"Percentage : {round(percent,2)}%")

    if percent >= 50:
        print("Status     : PASS")
    else:
        print("Status     : FAIL")

# ------------------ Results ------------------

def view_results(user):
    print("\n========= RESULT HISTORY =========")
    results = users_db[user]["results"]

    if not results:
        print("No exam records found.")
    else:
        for r in results:
            print(f"""
Subject    : {r['subject']}
Score      : {r['score']}/{r['total']}
Percentage : {r['percentage']}%
Date       : {r['date']}
---------------------------
""")

# ------------------ Main System ------------------

def online_exam_system():
    while True:
        user = login()
        if user:
            while True:
                menu()
                ch = input("\nChoose Option (1-4): ")

                if ch == "1":
                    view_subjects()
                elif ch == "2":
                    start_exam(user)
                elif ch == "3":
                    view_results(user)
                elif ch == "4":
                    print("\nThank you for using Online Examination System!")
                    time.sleep(1)
                    break
                else:
                    print("Invalid Option!")

                input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
online_exam_system()
