import random

difficulties = ["easy", "medium", "hard"]
user_input = input("What difficulty do you want to chose?\n")

while user_input not in difficulties:

  user_input = input("Type in easy, medium, or hard.\n")

print("You picked " + user_input + " mode. Good luck!\n")

difficulty = 1

if user_input == "easy":
  difficulty = 10
elif user_input == "medium":
  difficulty = 100
elif user_input == "hard":
  difficulty =1000
else: 
  print("Something went wrong. Flipping a coin")

print("Guess between 0 and " + str(difficulty))

random_number = random.randint(0,difficulty)

user_guess = int(input("Guess a number.\n"))

num_guesses = 1

while user_guess != random_number:

  if user_guess > random_number:
    user_guess = int(input("haha you got it wrong guess a smaller number\n"))
  elif user_guess < random_number:
    user_guess = int(input("haha you got it wrong guess a bigger number\n"))
  else:
    break
  num_guesses = 1 + num_guesses
  
print("Finally! Congratulations, you won, it took you " + str(num_guesses) + " tries.")