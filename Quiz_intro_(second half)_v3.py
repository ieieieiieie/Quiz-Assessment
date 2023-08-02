
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

answer = user_answer("would you like to see the introduction? ")
if answer == "yes":
  introduction()

print("program continues")