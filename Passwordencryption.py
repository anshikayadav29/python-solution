import os
from cryptography.fernet import Fernet

# ---------- STEP 1: CREATE OR LOAD KEY ----------
def load_key():
    """Load the encryption key from a file or generate a new one"""
    if not os.path.exists("key.key"):
        key = Fernet.generate_key()
        with open("key.key", "wb") as key_file:
            key_file.write(key)
    else:
        with open("key.key", "rb") as key_file:
            key = key_file.read()
    return key


# ---------- STEP 2: ENCRYPTION SETUP ----------
key = load_key()
fer = Fernet(key)


# ---------- STEP 3: ADD NEW PASSWORD ----------
def add_password():
    site = input("Enter site name: ").strip()
    username = input("Enter username: ").strip()
    password = input("Enter password: ").strip()

    with open("passwords.txt", "a") as f:
        encrypted_pass = fer.encrypt(password.encode()).decode()
        f.write(f"{site} | {username} | {encrypted_pass}\n")
    print("✅ Password saved securely!\n")


# ---------- STEP 4: VIEW SAVED PASSWORDS ----------
def view_passwords():
    if not os.path.exists("passwords.txt"):
        print("No passwords saved yet!\n")
        return

    with open("passwords.txt", "r") as f:
        for line in f.readlines():
            data = line.strip().split(" | ")
            site, username, encrypted_pass = data
            decrypted_pass = fer.decrypt(encrypted_pass.encode()).decode()
            print(f"🌐 Site: {site}\n👤 Username: {username}\n🔑 Password: {decrypted_pass}\n")


# ---------- STEP 5: MAIN MENU ----------
def main():
    print("🔒 Secure Password Manager 🔒")
    while True:
        print("1. Add new password")
        print("2. View passwords")
        print("3. Exit")
        choice = input("Enter choice: ").strip()

        if choice == "1":
            add_password()
        elif choice == "2":
            view_passwords()
        elif choice == "3":
            print("👋 Exiting... Stay secure!")
            break
        else:
            print("Invalid choice, try again!\n")


if __name__ == "__main__":
    main()
