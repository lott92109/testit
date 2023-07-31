import random
x = int(
    input(
        "Welcome to the guessing game. Please guess a whole number from 1 and 10."
    ))
y = int(random.randint(1, 10))
if x == y:
  print("Congratulation. You guessed correctly and won.")
elif x<1:
  print("You number you enter was smaller then 1. Pleas run the game again")
elif x >10:
  print ("Your number you enter was greater than 10. Pleas run the game again")
else:
  print("Sorry your guess was wrong. The number was", y)