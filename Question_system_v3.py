import time
points = 0 

q1 = input("The ___ is out of the bag, what is the missing word? ").lower()

if q1 == "cat":
  points += 1 
  print("{}...".format(q1))
  time.sleep(3)
  print("is the correct answer! +1 point!")

else:
  print("{}...".format(q1))
  time.sleep(3)
  print("is the incorrect answer! The correct answer was cat!")

time.sleep(5)
print()

q2 = input("The early ____ catches the worm, what is the missing word? ").lower()

if q2 == "bird":
  points += 1  
  print("{}...".format(q2))
  time.sleep(3)
  print("is the correct answer! +1 point!")

else:
  print("{}...".format(q2))
  time.sleep(5)
  print("is the incorrect answer! The correct answer was bird!")