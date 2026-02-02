
# E-Voting System - Python Project (Console Based)

import time
import random
from datetime import datetime

# ------------------ Databases ------------------

voters_db = {
    "V1001": {"name": "Ashim Shrestha", "voted": False},
    "V1002": {"name": "JIban Shrestha", "voted": False},
    "V1003": {"name": "Nabin Shrestha", "voted": False}
}

candidates_db = {
    "C1": {"name": "SUN", "votes": 0},
    "C2": {"name": "Moon", "votes": 0},
    "C3": {"name": "Earth", "votes": 0}
}

votes_log = []

# ------------------ Utilities ------------------

def loading():
    print("\nProcessing", end="")
    for _ in range(3):
        time.sleep(0.4)
        print(".", end="")
    print("\n")

# ------------------ Voter Login ------------------

def voter_login():
    print("\n====== E-Voting System ======")
    voter_id = input("Enter Voter ID: ")

    if voter_id in voters_db:
        print(f"Welcome, {voters_db[voter_id]['name']}")
        loading()
        return voter_id
    else:
        print("Invalid Voter ID!")
        return None

# ------------------ Menu ------------------

def menu():
    print("\n========= MENU =========")
    print("1. View Candidates")
    print("2. Cast Vote")
    print("3. View Results (Admin)")
    print("4. Exit")

# ------------------ Candidate List ------------------

def view_candidates():
    print("\n====== Candidate List ======")
    for cid, c in candidates_db.items():
        print(f"{cid}. {c['name']}")

# ------------------ Voting ------------------

def cast_vote(voter_id):
    if voters_db[voter_id]["voted"]:
        print("You have already voted! Duplicate voting not allowed.")
        return

    view_candidates()
    choice = input("\nEnter Candidate ID: ")

    if choice not in candidates_db:
        print("Invalid Candidate ID!")
        return

    candidates_db[choice]["votes"] += 1
    voters_db[voter_id]["voted"] = True

    vote_record = {
        "voter_id": voter_id,
        "candidate": candidates_db[choice]["name"],
        "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S")
    }

    votes_log.append(vote_record)

    loading()
    print("\n✅ Vote Cast Successfully!")
    print("Thank you for participating in the election.")

# ------------------ Results ------------------

def view_results():
    print("\n====== Election Results ======")
    for cid, c in candidates_db.items():
        print(f"{c['name']} : {c['votes']} votes")

    print("\n====== Vote Log (Admin) ======")
    for v in votes_log:
        print(f"Voter: {v['voter_id']} | Candidate: {v['candidate']} | Time: {v['time']}")

# ------------------ Main System ------------------

def evoting_system():
    while True:
        voter_id = voter_login()
        if voter_id:
            while True:
                menu()
                ch = input("\nChoose Option (1-4): ")

                if ch == "1":
                    view_candidates()
                elif ch == "2":
                    cast_vote(voter_id)
                elif ch == "3":
                    view_results()
                elif ch == "4":
                    print("\nThank you for using E-Voting System!")
                    time.sleep(1)
                    break
                else:
                    print("Invalid Option!")

                input("\nPress Enter to continue...")

# ------------------ Run Program ------------------
evoting_system()
