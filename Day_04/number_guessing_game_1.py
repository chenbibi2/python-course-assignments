import random
number= random.randint (1,20)
print ("I am thinking of a number between 1 and 20, can you guess what it is?" )
guess =0
while (number != guess):
 guess = int(input("your guess is:"))
 if guess < number:
        print("The number you entered is lower than what I chose.")
 elif guess > number:
        print("The number you entered is higher than what I chose.")
 else:
        print("Congratulations! You guessed the right number!")
