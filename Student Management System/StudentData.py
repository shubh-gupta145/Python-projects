class Student:
    def __init__(self,name,classes,marks,id):
        self.name = name
        self.classes = classes 
        self.marks = marks
        self.id = id 

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