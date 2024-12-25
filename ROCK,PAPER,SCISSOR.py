import random
options="RPS"
while True:
    choice=input("Enter your choice(ROCK, PAPER OR SCISSOR). Press 1 to quit:")
    comp = random.choice(options)
    if choice == '1':
        print("Quitting")
        break
    if choice == ("ROCK" and comp=="R") or (choice == "PAPER" and comp=="P") or (choice == "SCISSOR" and comp=="S"):
            print("DRAW")
    elif (choice == "ROCK" and comp=="P") or (choice == "SCISSOR" and comp=="R") or (choice == "PAPER" and comp=="S"):
            print("YOU LOSE")
    elif (choice == "ROCK" and comp=="S") or (choice == "PAPER" and comp=="R") or (choice == "SCISSOR" and comp=="P"):
            print("YOU WON")
    else:
            print("CHOOSE THE VALID OPTION")
