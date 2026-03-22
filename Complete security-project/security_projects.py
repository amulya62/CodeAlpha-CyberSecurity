import re
import hashlib
import getpass

# Hash password
def hash_password(password):
    return hashlib.sha256(password.encode()).hexdigest()

# Check password strength
def check_password_strength(password):
    strength = 0

    if len(password) >= 8:
        strength += 1
    if re.search("[A-Z]", password):
        strength += 1
    if re.search("[a-z]", password):
        strength += 1
    if re.search("[0-9]", password):
        strength += 1
    if re.search("[@#$%^&*!]", password):
        strength += 1

    if strength == 5:
        return "Strong"
    elif strength >= 3:
        return "Medium"
    else:
        return "Weak"

# Register user
def register():
    username = input("Enter username: ")
    password = getpass.getpass("Enter password: ")

    strength = check_password_strength(password)
    print("Password strength:", strength)

    if strength == "Weak":
        print("Choose a stronger password!")
        return

    # Check if username exists
    try:
        with open("users.txt", "r") as file:
            for user in file:
                stored_username, _ = user.strip().split(",")
                if username == stored_username:
                    print("Username already exists!")
                    return
    except FileNotFoundError:
        pass

    # Save hashed password
    hashed = hash_password(password)

    with open("users.txt", "a") as file:
        file.write(username + "," + hashed + "\n")

    print("Registration successful!")

# Login user
def login():
    try:
        with open("users.txt", "r") as file:
            users = file.readlines()
    except FileNotFoundError:
        print("No users found. Please register first.")
        return

    attempts = 3

    while attempts > 0:
        username = input("Enter username: ")
        password = getpass.getpass("Enter password: ")

        for user in users:
            stored_username, stored_password = user.strip().split(",")

            if username == stored_username and hash_password(password) == stored_password:
                print("Login successful 🎉")
                return

        attempts -= 1
        print("Invalid credentials. Attempts left:", attempts)

    print("Too many failed attempts!")

# Main menu
while True:
    print("\n1. Register")
    print("2. Login")
    print("3. Exit")

    choice = input("Enter choice: ")

    if choice == "1":
        register()
    elif choice == "2":
        login()
    elif choice == "3":
        print("Goodbye!")
        break
    else:
        print("Invalid choice")
