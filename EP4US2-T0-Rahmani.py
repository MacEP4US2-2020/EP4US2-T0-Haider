from random import randint
t = ["R", "P", "S"]
computer = t[randint(0,2)]
print("Welcome to the game of Rock-Paper-scissors")
human_input = input("Select your champion (R/P/S)")
if (human_input == "R") or (human_input == "P") or (human_input == "S"):
    print ("Computer chose:",computer)
    if (human_input == "R"):
            if (computer == "R"):
                print ("Tie!")
            elif (computer == "S"):
                print ("YOU WIN")
            elif (computer == "P"):
                print ("YOU LOOSE")
    elif (human_input == "P"):
            if (computer == "R"):
                print ("YOU WIN")
            elif (computer == "S"):
                print ("YOU LOOSE")
            elif (computer == "P"):
                print ("Tie!")
    if (human_input == "S"):
            if (computer == "R"):
                print ("YOU LOOSE!")
            elif (computer == "S"):
                print ("Tie!")
            elif (computer == "P"):
                print ("YOU WIN")
else: 
    print ("[ERROR] Invalid input, must be either R/P/S")
