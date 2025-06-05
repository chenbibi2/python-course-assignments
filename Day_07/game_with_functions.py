import random

def get_number():
    return random.randint(1, 20)

def guess_number(number):
    print("I am thinking of a number between 1 and 20, can you guess what it is?")
    while True:
        guess = int(input("Your guess is: "))
        if number < guess:
            print("The number you entered is lower than what I chose.")
        elif number > guess:
            print("The number you entered is higher than what I chose.")
        else:
            print("Congratulations! You guessed the right number!")
            break
        
number = get_number()
guess_number(number)
