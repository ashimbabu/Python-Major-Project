def login():
    print("\n===== Employee Management System Login =====")
    username = input("Username: ")
    password = input("Password: ")

    # simple authentication
    if username == "admin" and password == "admin123":
        print("\nLogin successful!\n")
        return True
    else:
        print("\nInvalid credentials!\n")
        return False