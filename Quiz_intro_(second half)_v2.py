
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
      

answer = user_answer("would you like to see the introduction? ")
print("user chose {}, executing appropriate response".format(answer))