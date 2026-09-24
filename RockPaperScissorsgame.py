import random
while True:
    if(userInput != "quit"):
        print("Thanks for playing! Goodbye!");
        break;
    print("🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥🔥");
    print("     ROCK • PAPER • SCISSORS");
    print("          ⚔️ VS ⚔️");
    print("       WHO WILL WIN? 🏆");
    print("🔥🔥🔥🔥 🔥🔥🔥🔥🔥🔥");
    list = ["Rock","Paper","Scisorrs"];
    randomChoice = random.choice(list);
    userInput = input("Enter your choice for Playing a Game Play or type 'Quit' to exit: ").lower()
    if(userInput == "play"):
        choice = input ("Enter your choice (Rock, Paper, Scissors): ").lower()
        if(choice == "rock" and randomChoice == "Paper"):
            print("You are loss the Game")
        elif (choice == "rock" and randomChoice == "Scisorrs"):
            print("You are Win the Game")
        else:
            print("Draw")
