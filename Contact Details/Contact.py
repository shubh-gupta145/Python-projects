Choice = True

while Choice:

    print("======== Contact Details ========")
    print(" ")
    print("1. Add The New Contact.")
    print("2. View all Contacts.")
    print("3. Search Contact.")
    print("4. Update Contact.")
    print("5. Delete Contact.")
    print("6. Exit. ")
    print(" ")
    print("=================================")

    Contact = {}

    UserChoice = int(input("Enter the Your Choice --> "))

    if (UserChoice == 1 ):
        class Contact:

            def __init__(self,ContactName,ContactNumb,ContactEmail,favorite):
                self.ContactName = ContactName
                self.ContactNumb = ContactNumb  
                self.ContactEmail = ContactEmail
                self.favorite = favorite
        while choice == 'yes':

            print("==========  Add The Contact  ==========")

            ContactName = input(" Enter the Contact Name --> ")
            ContactNumb = int(input("Enter The Contact Number -->"))
            ContactEmail = input("Enter The Contact Email --> ")
            favorite = input("Enter The Favorite List in Your Contact 'YES' or 'NO' ")

            choice = input("Do you want to add another contact? (yes/no): ").lower()
            if choice != 'no':
                breakpoint

    elif(UserChoice == 2 ):
        print(s1.ContactName)
        print(s1.ContactNumb)
        print(s1.ContactEmail)
        print(s1.favorite)

    elif(UserChoice == 3):

    elif(UserChoice == 4):
    elif(UserChoice == 5):
    elif(UserChoice == 6):
        Choice = False
