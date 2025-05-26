import random
number = random.randint(1, 20)
print("I am thinking of a number between 1 and 20. Can you guess what it is?")
print("Type 'x' to quit the game.")
print("Type 's' to reveal the number.")
print("Type 'd' to enter debug mode.")
print("Type 'm' to enter move mode")
print("Type 'n' to start a new game")
debug = False
move = False 
m_options = [-2, -1, 0, 1, 2]
while True:
    if debug:
        print(f"(Debug Mode) The number is {number}")
    if move:
      number += random.choice(m_options)
      number =max(1, min(number, 20))
      
    guess = input("Your guess is: ")
    if guess == "x":
        print("You quit the game.")
        break
    elif guess == "s":
        print(f"The number is: {number}")
        break
    elif guess == "d":
        debug = not debug
        if debug:
            print("Debug mode is now ON.")
        else:
            print("Debug mode is now OFF.")
    elif guess == "m":
        move = not move
        if move:
            print("move mode is now ON.")
        else:
            print("move mode is now OFF.")
    elif: guess == "n":
      number= random.randint(1, 20)
      print ("starting a new game")
      debug = False
      move = False
      continue
    elif guess.isdigit():
        guess = int(guess)
        if guess < number:
            print("The number you entered is lower than what I chose.")
        elif guess > number:
            print("The number you entered is higher than what I chose.")
        else:
            print("Congratulations! You guessed the right number!")
            break

