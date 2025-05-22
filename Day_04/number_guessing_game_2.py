import random
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20. Can you guess what it is?")
print("Type 'x' to quit the game.")
while True:
    guess = input("Your guess is: ")
    if guess.lower() == "x":
        print("You quit the game.")
        break
    else:
        guess = int(guess)      
    if guess < number:
        print("The number you entered is lower than what I chose.")
    elif guess > number:
        print("The number you entered is higher than what I chose.")
    else:
        print("Congratulations! You guessed the right number!")
        break
