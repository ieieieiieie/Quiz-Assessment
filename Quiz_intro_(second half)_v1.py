print("Thank you for entering your name")

valid = False
while not valid:
  answer = input("Would you like to hear the quiz introduction? ").lower()
  
  if answer == "yes" or answer == "y":
    valid = True
    print("display intro")
  
  elif answer == "no" or answer == "n":
    valid = True
    print("skip intro")
  
  else:
    print("loop code")