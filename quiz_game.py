print("welcome to my computer quiz!")

playing = input("Do you want to play? ").lower()
score = 0

if playing != "yes":
    quit()

print("Come On. Let's Play ")

answer = input("What is the capital of India? ").lower()
if answer == "new delhi":
    score = score + 1
    print('Correct!')
else:
    print('Incorrect!')    

answer = input("What is the national bird of India? ").lower()
if answer == "peacock":
    score = score + 1
    print('Correct!')
else:
    print('Incorrect!')    

answer = input("What is the national animal of India? ").lower()
if answer == "tiger":
    score += 1
    print('Correct!')
else:
    print('Incorrect!')    

print(f"Game completed! Your score is {((score/3)*100):.2f}%")

