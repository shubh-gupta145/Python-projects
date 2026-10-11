import random
difficulty = "E"
while difficulty!="Q":
    print("<--------Welcome to the guess the number Game------->")
    print()
    print()
    print("║         SELECT YOUR DIFFICULTY LEVEL      ║")
    print("╠" + "═" * 43 + "╣")
    print("║  🟢 [E]asy  🟡 [M]edium  🟠 [H]ard  🔴 [X]treme  🛑 [Q]uit  ║")
    print()
    print("╚" + "═" * 43 + "╝")

    difficulty = input("👉 Enter choice (E/M/H/X/Q): ").strip().upper()

    if(difficulty=="E"):
        print("Number is Present Between 1 to 1000")
        rightNumber = random.randint(1, 1000)
        chances = 20
        while chances != 0 :
            GuessNumber = int(input("Enter your guess number: "))
            if(GuessNumber==rightNumber):
                print("<------Congratulation you are win the Game------>")
                breakpoint
            elif(GuessNumber>rightNumber):
                print("Your Number is Greater Then the Right Number")
                chances = chances - 1
                print("You have", chances, "chances left")
            else:
                print("Your Number is smaller Then the Right Number")
                chances = chances - 1
                print("You have", chances, "chances left")

    elif(difficulty=="M"):
        print("Number is Present Between 1 to 10000")
        rightNumber = random.randint(1, 10000)
        chances = 15
        while chances != 0 :
            GuessNumber = int(input("Enter your guess number: "))
            if(GuessNumber==rightNumber):
                print("<------Congratulation you are win the Game------>")
                breakpoint
            elif(GuessNumber>rightNumber):
                print("Your Number is Greater Then the Right Number")
                chances = chances - 1
                print("You have", chances, "chances left")
            else:
                print("Your Number is smaller Then the Right Number")
                chances = chances - 1
                print("You have", chances, "chances left")

    elif(difficulty=="H"):
        print("Number is Present Between 1 to 100000")
        rightNumber = random.randint(1, 100000)
        chances = 10    
        while chances != 0 :
            GuessNumber = int(input("Enter your guess number: "))
            if(GuessNumber==rightNumber):
                print("<------Congratulation you are win the Game------>")
                breakpoint
            elif(GuessNumber>rightNumber):
                print("Your Number is Greater Then the Right Number")
                chances = chances - 1
                print("You have", chances, "chances left")
            else:
                print("Your Number is smaller Then the Right Number")
                chances = chances - 1
                print("You have", chances, "chances left")

    elif(difficulty=="X"):
        print("Number is Present Between 1 to 1000000")
        rightNumber = random.randint(1, 1000000)
        chances = 5
        while chances != 0 :
            GuessNumber = int(input("Enter your guess number: "))
            if(GuessNumber==rightNumber):
                print("<------Congratulation you are win the Game------>")
                breakpoint
            elif(GuessNumber>rightNumber):
                print("Your Number is Greater Then the Right Number")
                chances = chances - 1
                print("You have", chances, "chances left")
            else:
                print("Your Number is smaller Then the Right Number")
                chances = chances - 1
                print("You have", chances, "chances left")

    elif(difficulty=="Q"):
        print("Exiting the game...")
        break