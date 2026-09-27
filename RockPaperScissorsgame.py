import random

while True:

    print("\n" + "🔥" * 12)
    print("     ROCK • PAPER • SCISSORS")
    print()
    print("           ⚔️  VS  ⚔️")
    print()
    print("        WHO WILL WIN? 🏆")
    print("🔥" * 12)
    print()

    choice = ["rock", "paper", "scissors"]
    randomChoice = random.choice(choice)

    userInput = input(
        "Enter 'Play' to start the game or type 'Quit' to exit: "
    ).lower()

    if userInput == "quit":
        print("\nThanks for playing! Goodbye! 👋")
        break

    if userInput == "play":

        choice = input(
            "\nEnter your choice (Rock, Paper, Scissors): "
        ).lower()

        if choice == "rock" and randomChoice == "paper":

            print("\n╔══════════════════════════════════╗")
            print("║          💀 GAME OVER!           ║")
            print("║       😔 YOU LOST THE GAME!      ║")
            print("║      Better luck next time! 🔥   ║")
            print("╚══════════════════════════════════╝")

        elif choice == "rock" and randomChoice == "scissors":

            print("\n╔══════════════════════════════════╗")
            print("║       🎉 CONGRATULATIONS! 🎉     ║")
            print("║          🏆 YOU WON! 🏆          ║")
            print("╚══════════════════════════════════╝")

        elif choice == "rock" and randomChoice == "rock":

            print("\n╔══════════════════════════════════╗")
            print("║          ⚔️  RESULT  ⚔️          ║")
            print("║        🤝 IT'S A DRAW! 🤝        ║")
            print("╚══════════════════════════════════╝")

        if choice == "paper" and randomChoice == "scissors":

            print("\n╔══════════════════════════════════╗")
            print("║          💀 GAME OVER!           ║")
            print("║       😔 YOU LOST THE GAME!      ║")
            print("║      Better luck next time! 🔥   ║")
            print("╚══════════════════════════════════╝")

        elif choice == "paper" and randomChoice == "rock":

            print("\n╔══════════════════════════════════╗")
            print("║       🎉 CONGRATULATIONS! 🎉     ║")
            print("║          🏆 YOU WON! 🏆          ║")
            print("╚══════════════════════════════════╝")

        elif choice == "paper" and randomChoice == "paper":

            print("\n╔══════════════════════════════════╗")
            print("║          ⚔️  RESULT  ⚔️          ║")
            print("║        🤝 IT'S A DRAW! 🤝        ║")
            print("╚══════════════════════════════════╝")

        if choice == "scissors" and randomChoice == "rock":

            print("\n╔══════════════════════════════════╗")
            print("║          💀 GAME OVER!           ║")
            print("║       😔 YOU LOST THE GAME!      ║")
            print("║      Better luck next time! 🔥   ║")
            print("╚══════════════════════════════════╝")

        elif choice == "scissors" and randomChoice == "paper":

            print("\n╔══════════════════════════════════╗")
            print("║       🎉 CONGRATULATIONS! 🎉     ║")
            print("║          🏆 YOU WON! 🏆          ║")
            print("╚══════════════════════════════════╝")

        elif choice == "scissors" and randomChoice == "scissors":

            print("\n╔══════════════════════════════════╗")
            print("║          ⚔️  RESULT  ⚔️          ║")
            print("║        🤝 IT'S A DRAW! 🤝        ║")
            print("╚══════════════════════════════════╝")