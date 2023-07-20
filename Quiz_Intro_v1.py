print("hello there! Welcome to our quiz.")

valid = False
while not valid:
  player_name = input("What is your name? ")

  if player_name.isalpha():
    valid = True
    print("display quiz introduction")

  else:
    print("please try again")