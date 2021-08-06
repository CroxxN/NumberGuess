import random
guess = ""
def value():
  global guess
  guess1 = random.randint(1, 100)
  guess = guess1
  return guess
def game():
  usr_value= int(input("Make a guess: "))
  if usr_value == guess:
    print("Correct value")
    value()
  elif usr_value > guess:
    print(f"{usr_value} is too high")
    game()
  elif usr_value < guess:
    print(f"{usr_value} is too low")
    game()
  choice = input("Continue? (y/n)")
  if choice.lower() == "y":
    game()
value()
game()

  