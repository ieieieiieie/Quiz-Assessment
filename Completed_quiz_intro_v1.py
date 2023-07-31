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

def user_answer(question):
  valid = False
  while not valid:
    answer = input(question)

    if answer == "yes" or answer == "y":
      answer = "yes"
      return answer 
   
    elif answer == "no" or answer == "n":
      answer = "no"
      return answer

    else:
      print("please answer yes / no")

def introduction():
  print("~~~INTRODUCTION~~~")
  print()
  print("insert intro here")
  print()
  print("~~~~~~~~~~~~~~~~~~")
  return ""

#main routine
player_name = p_name("Please enter your name (letters only) ")
print("{} is a valid name, thank you for entering {}.".format(player_name , player_name))

answer = user_answer("would you like to see the introduction? ")
if answer == "yes":
  introduction()

print("program continues")