name = input("Enter your name: ")
print("Welcome", name, "to your own adventure")

answer = input("you are at the end of dirt road, Move left/right. ")
if answer == "left":
    answer = input("you came to river. Swim/move. ")
    if answer == "swim":
        print("you're eaten by Blue Whale. You Lose!")
    elif answer == "move":
        answer = input("you come across the bridge. cross/go back ")
        if answer =="cross":
            print("You won!")
        elif answer == "go back":
            print("you lose!")
        else:
            print("Not a valid option. You Lose!")            
    else:
        print("Not a valid option. You Lose!")        
elif answer == "right":
    print("DANGER. You Lose!")
else:
    print("Not a valid option. You Lose!")        