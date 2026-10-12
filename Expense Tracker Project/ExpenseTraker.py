print("=====  Expense Tracker  ===== \n\n\n")
print(" 1. Add Expense\n 2. View All the Expense\n 3. Calculate Total Expense\n 4. Exit\n 5. For Deleting the Expense Item")
UserChoice = True
while UserChoice :
    CustomerChoice = int(input("Choose an Option :--> "))

    if(CustomerChoice == 1):
        ExpenseItem = input(("Enter the Expense Item Name :-->"))
        ExpenseAmount = int(input("Enter the Amount :--> "))
        ItemDetailsFile = open("ExpenseItemDetails.txt", "a")
        ItemDetailsFile.write(ExpenseItem + "\n")
        ItemDetailsFile.close()
        ItemExpenseFile = open("ExpenseItem.txt","a")
        ItemExpenseFile.write(str(ExpenseAmount) + "\n")
        ItemExpenseFile.close()
        print("Expense Item Added Successfully")

    elif(CustomerChoice == 2 ):
        with open("ExpenseItemDetails.txt", "r") as ItemDetailsFile:
            ExpenseItemList = ItemDetailsFile.readlines()
            print(ExpenseItemList)

    elif(CustomerChoice == 3):
        with open("ExpenseItem.txt", "r") as ItemExpenseFile:
            ExpenseAmountList = ItemExpenseFile.readlines()
            TotalExpense = sum(int(amount) for amount in ExpenseAmountList)
            print("Total Expense is :--> ", TotalExpense)
        
    elif(CustomerChoice == 5):
        with open("ExpenseItemDetails.txt", "w") as file:
            pass
        with open("ExpenseItem.txt", "w") as file:
            pass
        UserChoice = False
    
    else:
        print("Thank You for Using Expense Tracker")
        UserChoice = False   