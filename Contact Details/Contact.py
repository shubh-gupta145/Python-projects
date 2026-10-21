class Contact:
    def __init__(self, name, number, email, favorite):
        self.name = name
        self.number = number
        self.email = email
        self.favorite = favorite

    def display(self):
        print(f"Name     : {self.name}")
        print(f"Number   : {self.number}")
        print(f"Email    : {self.email}")
        print(f"Favorite : {self.favorite}")
        print("-" * 30)


contacts = []  

while True:
    print("\n======== Contact Book ========")
    print("1. Add Contact")
    print("2. View all Contacts")
    print("3. Search Contact")
    print("4. Update Contact")
    print("5. Delete Contact")
    print("6. Exit")
    print("==============================")

    try:
        choice = int(input("Enter your choice --> "))
    except ValueError:
        print("Please enter a number.")
        continue

    if choice == 1:
        while True:
            name = input("Enter name --> ")
            number = input("Enter number --> ")   
            email = input("Enter email --> ")
            fav = input("Favorite? (yes/no) --> ")

            contacts.append(Contact(name, number, email, fav))
            print("Contact added! Successfully.")

            again = input("Add another? (yes/no): ").lower()
            if again == "no":
                break

    elif choice == 2:
        if not contacts:
            print("No contacts yet.")
        for c in contacts:
            c.display()

    elif choice == 3:
        key = input("Enter name to search --> ").lower()
        found = False
        for c in contacts:
            if key in c.name.lower():
                c.display()
                found = True
        if not found:
            print("Not found.")

    elif choice == 4:
        key = input("Enter exact name to update --> ").lower()
        for c in contacts:
            if c.name.lower() == key:
                c.name = input("New name --> ")
                c.number = input("New number --> ")
                c.email = input("New email --> ")
                c.favorite = input("Favorite? (yes/no) --> ")
                print("Updated!")
                break
        else:
            print("Not found.")

    elif choice == 5:
        key = input("Enter exact name to delete --> ").lower()
        for c in contacts:
            if c.name.lower() == key:
                contacts.remove(c)
                print("Deleted!")
                break
        else:
            print("Not found.")

    elif choice == 6:
        print("Goodbye!")
        break