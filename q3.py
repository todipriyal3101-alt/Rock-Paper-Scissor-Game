#rock, paper, scissor game
import random
choices = ["🪨", "📃", "✂️"]


while True: 
    comp = random.choice(choices)
    choice = input("Rock, Paper or Scissors? (r/p/s):  ")
    if choice == "r":
        a = "You chose 🪨"
        b = "Computer Chose "+ comp
        print(a)
        print(b)
        if comp == "📃":
            print("You lost the game")
        elif comp == "✂️":
            print("You win the game")
        else:
            print("Its a tie")
            
    elif choice == "p":
        c = "You chose 📃"
        d = "Computer Chose "+ comp
        print(c)
        print(d)
        if comp == "🪨":
            print("You win the game")
        elif comp == "✂️":
            print("You lost the game")
        else:
            print("Its a tie")
            
    elif choice == "s":
        e = "You chose ✂️"
        f = "Computer Chose " + comp
        print(e)
        print(f)
        if comp == "🪨":
            print("You lost the game")
        elif comp == "📃":
            print("You win the game")
        else:
            print("Its a tie")


    again = input("Do you want to continue the game? (y/n): ")
    if again == "y" or again == "Y":
        continue
    elif again == "n" or again == "N":
        print("Thank You for playing")
        print("The game ends.......")
        break
    else:
        print("Invalid input")
        print("The game ends")
        break
