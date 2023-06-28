import random

user_wins = 0
computer_wins = 0

options =["rock", "paper", "scissor"]
i=0
while True:
    if i == 0:
        games = int(input("How many games you want to play: "))
    i += 1    
    if i == (games+1):
        break 
    computer_input = options[random.randint(0,2)]
    user_input = input("Choose rock/paper/scissor or q to Quit ")
    if user_input == "q":
        break
    if user_input not in options:
        continue
    if user_input == computer_input:
        print("Draw!")
        continue
    if (computer_input =="scissor" and user_input =="rock") or (computer_input =="paper" and user_input =="scissor") or (computer_input =="rock" and user_input =="paper"):
        user_wins += 1
        print("you Win!")
    else:
        computer_wins += 1
        print("you Lose")  
print("your score is", user_wins)
print("computer score is", computer_wins)      

       