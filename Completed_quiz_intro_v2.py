#time module to create pauses between prints
import time

#functions go here

#function to get the player's name
def p_name(question):
  valid = False
  while not valid:
    player_name = input(question)

    if player_name.isalpha():
      valid = True
      return player_name

    else:
      print("{} is not a valid name".format(player_name))

#function to get the player's answer on displaying the introduction
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

#function for the introduction display
def introduction():
  print("~~~INTRODUCTION~~~")
  print()
  print("insert intro here")
  print()
  print("~~~~~~~~~~~~~~~~~~")
  return ""

#main routine

#response after successfully picking a valid name
player_name = p_name("Please enter your name (letters only) ")
time.sleep(2)
print("{} is a valid name, thank you for entering {}.".format(player_name , player_name))
print()

#code to display or to not display the instructions accordingly
answer = user_answer("would you like to see the introduction? ")
if answer == "yes":
  time.sleep(1)
  print()
  introduction()

#print statement to move to the next component
time.sleep(1)
print("program continues")