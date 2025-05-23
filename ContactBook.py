import os

CONTACTS_FILE = "contacts.txt"

def add_contact():
    name = input("Enter name: ")
    phone = input("Enter phone number: ")
    email = input("Enter email address: ")

    with open(CONTACTS_FILE, "a") as file:
        file.write(f"{name},{phone},{email}\n")
    print("✅ Contact added successfully!\n")

def view_contacts():
    if not os.path.exists(CONTACTS_FILE):
        print("No contacts found.\n")
        return

    print("\n📇 Contact List:")
    with open(CONTACTS_FILE, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            print(f"Name: {name}, Phone: {phone}, Email: {email}")
    print()

def search_contact():
    search_name = input("Enter name to search: ").lower()
    found = False

    with open(CONTACTS_FILE, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            if search_name in name.lower():
                print(f"✅ Found: Name: {name}, Phone: {phone}, Email: {email}")
                found = True
    if not found:
        print("❌ No contact found with that name.\n")

def delete_contact():
    delete_name = input("Enter name to delete: ").lower()
    contacts = []
    found = False

    with open(CONTACTS_FILE, "r") as file:
        for line in file:
            name, phone, email = line.strip().split(",")
            if delete_name != name.lower():
                contacts.append(line)
            else:
                found = True

    with open(CONTACTS_FILE, "w") as file:
        file.writelines(contacts)

    if found:
        print("🗑️ Contact deleted successfully.\n")
    else:
        print("❌ Contact not found.\n")

def main():
    while True:
        print("=== Contact Book Menu ===")
        print("1. Add Contact")
        print("2. View Contacts")
        print("3. Search Contact")
        print("4. Delete Contact")
        print("5. Exit")

        choice = input("Enter your choice (1-5): ")

        if choice == '1':
            add_contact()
        elif choice == '2':
            view_contacts()
        elif choice == '3':
            search_contact()
        elif choice == '4':
            delete_contact()
        elif choice == '5':
            print("👋 Exiting Contact Book. Goodbye!")
            break
        else:
            print("❌ Invalid choice. Please try again.\n")

if __name__ == "__main__":
    main()
