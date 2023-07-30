import random
x = int(
    input(
        "Welcome to the guessing game. Please guess a a whole number from 1 and 10."
    ))
y = int(random.randint(0, 10))
if x == y:
  print("Congratulation. You guessed correctly and won.")
else:
  print("Sorry your guess was wrong. The number was", y)