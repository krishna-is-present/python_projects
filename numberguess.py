
print("Welcome to the Number Guessing Game!")
print("I'm thinking of a number between 1 and 100")

from random import randint

select = input("Choose a difficulty. Type 'easy' or 'hard': \n")

if select == "easy":
  a = 10
elif select == "hard":
  a = 5


def guess(b):
  number = randint(1,100)
  print(f"You have {b} attempts remaining to guess the number")
  while True:
    choice = int(input("Make a guess: \n"))
    if number == choice:
      print(f"You got it! The answer was {number}")
      return
    elif number > choice and b == 1:
      print("Too low. \nYou've run out of guesses, you lose")
      return
    elif number < choice and b == 1:
      print("Too high. \nYou've run out of guesses, you lose")
      return
    elif number > choice:
      print("Too low. Guess again")
      b -= 1
      print(f"You have {b} attempts remaining to guess the number")
    elif number < choice:
      print("Too high. Guess again")
      b -= 1
      print(f"You have {b} attempts remaining to guess the number")

guess(a)
