number = 1
while number != 0:
    print("Please Enter the Integer values not a Special Characters or Float values")
    value1 = int(input("Enter the first value: "))
    value2 = int(input("Enter the second value: "))
    operation = input("Enter the operation (+, -, *, /,0 to exit): ")
    if operation == "0":
        number = 0
        print("Now you are exiting the program")
        break
    match operation:
        case "+":
            result = value1 + value2
        case "-":
            result = value1 - value2
        case "*":
            result = value1 * value2
        case "/":
            if value2 != 0:
                result = value1 / value2
            else:
                result = "Error: Division by zero"
    print("This is your final Output:", result)