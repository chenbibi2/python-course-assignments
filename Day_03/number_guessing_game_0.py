import random
number= random.randint (1,20)
  print ("I am thinking of a number between 1 and 20, can you guess what it is?" )
  guess = int(input("your guess is:"))
  if number < guess:
    print ("The number you entered is lower than what I chose")
  elif number > guess:
    print ("The number you entered is higher than what I chose")
    else :
    print("Congratulations! You guessed the right number!")
