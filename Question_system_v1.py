correct = "cat"

question_1 = input("The ___ is out of the bag, what is the missing word? ").lower()

if question_1 == correct:
  print("that is the correct answer! +1 point!")

else:
  print("that is incorrect, the correct answer is {}.".format(correct))
  