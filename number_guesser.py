import random

print("Welcome to number guesser game")

top_range = input("Enter a number: ")
if top_range.isdigit():
    top_range = int(top_range)
elif top_range < 0:
    print("Enter a number greater than zero")
    quit()
else:
    print("Enter a number")
    quit()

random_number = random.randint(0,top_range)
guesses =0

while True:
    user_guess = input("Guess a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    elif user_guess < 0:
        print("Enter a number greater than zero")
        continue
    else:
        print("Enter a number")
        continue

    guesses += 1

    if user_guess == random_number:
        print("You got a number in", guesses, "guesses")
        quit()
    else:
        if user_guess < random_number:
            print("Wrong! Number is greater than this.")
        else:
            print("Wrong! number is lesser than this.")    
