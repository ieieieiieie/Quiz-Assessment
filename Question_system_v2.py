correct = "cat"
correct2 = "bird"
points = 0 

question_1 = input("The ___ is out of the bag, what is the missing word? ").lower()

if question_1 == correct:
  points += 1 
  print("that is the correct answer! +1 point!")

else:
  print("that is an incorrect answer! the correct answer is {}.".format(correct))

print()

question2 = input("The early ____ catches the worm, what is the missing word? ").lower()

if question2 == correct2:
  points += 1
  print("that is the correct answer! +1 point!")

else:
  print("that is an incorrect answer! the correct answer is {}.".format(correct2))

print()
print("your final score is {}! thanks for playing!".format(points))