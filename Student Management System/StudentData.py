class Student:
    def __init__(self,name,classes,marks,id):
        self.name = name
        self.classes = classes 
        self.marks = marks
        self.id = id 
    def display(self):
        print(f"Name     : {self.name}")
        print(f"Classes  : {self.classes}")
        print(f"Marks    : {self.marks}")
        print(f"Id       : {self.id}")
        print("-" * 30)

student = []

while True:

    print("=======  Student Management System  =======")
    print("  ")
    print("  ")
    print(" 1. Add Student ")
    print(" 2. View The Student ")
    print(" 3. Search Student ")
    print(" 4. Update Your Mark ")
    print(" 5. Delete Student ")
    print(" 6. Calculate Average ")
    print(" 7. Find Topper ")
    print(" 8. Assign Grades ")
    print(" 9. Sort Student By Marks ")
    print(" 10. Exit ")
    UserChoice = int(input("Enter the your Choice --> "))
    if(UserChoice == 1):
        while True: 
            name = input("Enter the Stuent name --> ")
            classes = int(input("Enter the Stuent classes --> "))
            marks = int(input("Enter the Stuent marks --> "))
            id = int(input("Enter the Stuent id --> "))
            student.append(name,classes,marks,id)
            print(" Student Successfully Added In Your Management System ")
            print("Now You want to add new more Student ")
            choice = input("Enter The Choice  'yes' or 'no' ").lower()
            if(choice == 'no'):
                break;
    elif(UserChoice == 2 ):
        if not student:
            print("No Student yet.")
        for s in student:
            s.display()
    elif(UserChoice == 3 ):
        searchStudent = input("Enter the Student Name Which is You Want to Search --> ").lower()
        for s in student:
            if searchStudent in s.name.lower():
                print()
            if not
    elif(UserChoice == 4 ):
    elif(UserChoice == 5 ):
    elif(UserChoice == 6 ):
    elif(UserChoice == 7 ):
    elif(UserChoice == 8 ):
    elif(UserChoice == 9 ):
    elif(UserChoice == 10 ):
        break;