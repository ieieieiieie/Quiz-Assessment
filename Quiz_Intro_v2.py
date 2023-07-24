#functions go here
def p_name(question):
  valid = False
  while not valid:
    player_name = input(question)

    if player_name.isalpha():
      valid = True
      return player_name

    else:
      print("{} is not a valid name".format(player_name))


#main routine
player_name = p_name("Please enter your name (letters only) ")
print("{} is a valid name".format(player_name))
