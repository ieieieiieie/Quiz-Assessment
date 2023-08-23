import time
import random
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

time.sleep(5)
print()

q3 = input("Easy as ___, what is the missing word? ").lower()

if q3 == "pie":
  points += 1 
  print("{}...".format(q3))
  time.sleep(3)
  print("is the correct answer! +1 point!")

else:
  print("{}...".format(q3))
  time.sleep(3)
  print("is the incorrect answer! The correct answer was pie!")

time.sleep(5)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Its time to ramp things up! Have you gotten used to the quiz yet?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)

print("from this point forward, all the questions will be random!")
time.sleep(1)
print()
print("Get ready!")

time.sleep(5)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("It's a piece of ____, what is the missing word? ").lower()
    
    if q1 == "cake":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was cake!")
      valid = True

  elif chosen == "q2":
    q2 = input("That's a ____ for your buck, what's the missing word? ").lower()

    if q2 == "bang":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was bang!")
      valid = True

  else:
    q3 = input("Something _____ is going on, what is the missing word? ").lower()
    if q3 == "fishy":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was fishy!")
      valid = True

time.sleep(5)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("A ____ a dozen, what is the missing word? ").lower()
    
    if q1 == "dime":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was cake!")
      valid = True

  elif chosen == "q2":
    q2 = input("Stop _______ around, what is the missing word? ").lower()

    if q2 == "mucking":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was bang!")
      valid = True

  else:
    q3 = input("Time to ___ in, what is the missing word? ").lower()
    if q3 == "dig":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was fishy!")
      valid = True

time.sleep(3)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("hold your ______, what is the missing word? ").lower()
    
    if q1 == "horses":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was horses!")
      valid = True

  elif chosen == "q2":
    q2 = input("all is fair in love and ___, what's the missing word? ").lower()

    if q2 == "war":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was war!")
      valid = True

  else:
    q3 = input("Spill the _____, what is the missing word? ").lower()
    if q3 == "beans":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was beans!")
      valid = True

time.sleep(5)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("Let's find the ____ of the problem, what is the missing word? ").lower()
    
    if q1 == "root":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was root!")
      valid = True

  elif chosen == "q2":
    q2 = input("_____ doesn't grow on trees, what's the missing word? ").lower()

    if q2 == "money":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was money!")
      valid = True

  else:
    q3 = input("Do you have ants in your _____? what is the missing word? ").lower()
    if q3 == "pants":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was ants!")
      valid = True

time.sleep(5)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("Take a _____ pill, what is the missing word? ").lower()
    
    if q1 == "chill":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was chill!")
      valid = True

  elif chosen == "q2":
    q2 = input("that joke was so ______, what's the missing word? ").lower()

    if q2 == "cheesy":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was cheesy!")
      valid = True

  else:
    q3 = input("______ again! what is the missing word? ").lower()
    if q3 == "foiled":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was foiled!")
      valid = True

time.sleep(5)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("Blow off some _____, what is the missing word? ").lower()
    
    if q1 == "steam":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was steam!")
      valid = True

  elif chosen == "q2":
    q2 = input("___, skip and a jump, what's the missing word? ").lower()

    if q2 == "hop":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was hop!")
      valid = True

  else:
    q3 = input("Bob's your _____ what is the missing word? ").lower()
    if q3 == "uncle":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was uncle!")
      valid = True

time.sleep(5)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("Beat around the ____, what is the missing word? ").lower()
    
    if q1 == "bush":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was bush!")
      valid = True

  elif chosen == "q2":
    q2 = input("let's bite the ______, what's the missing word? ").lower()

    if q2 == "bullet":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was bullet!")
      valid = True

  else:
    q3 = input("back to the _______ board, what is the missing word? ").lower()
    if q3 == "drawing":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was drawing!")
      valid = True

time.sleep(5)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("Going on a wild _____ chase, what is the missing word? ").lower()
    
    if q1 == "goose":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was goose!")
      valid = True

  elif chosen == "q2":
    q2 = input("Are you under the _______? what's the missing word? ").lower()

    if q2 == "weather":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was weather!")
      valid = True

  else:
    q3 = input("You're pulling my ___, what is the missing word? ").lower()
    if q3 == "leg":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was leg!")
      valid = True

time.sleep(5)
print()
questions = ("q1", "q2", "q3")
chosen = random.choice(questions)

valid = False
while not valid:
  if chosen == "q1":
    q1 = input("Let's go the whole ____ yards, what is the missing word? ").lower()
    
    if q1 == "nine":
      print("{}...".format(q1))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True
    
    else:
      print("{}...".format(q1))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was nine!")
      valid = True

  elif chosen == "q2":
    q2 = input("________ killed the cat, what's the missing word? ").lower()

    if q2 == "curiosity":
      print("{}...".format(q2))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1 
      valid = True
    
    else:
      print("{}...".format(q2))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was curiosity!")
      valid = True

  else:
    q3 = input("Every ___ has his day, what is the missing word? ").lower()
    if q3 == "dog":
      print("{}...".format(q3))
      time.sleep(3)
      print("is the correct answer! +1 point!")
      points += 1
      valid = True

    else:
      print("{}...".format(q3))
      time.sleep(3)
      print("is the incorrect answer! The correct answer was dog!")
      valid = True

time.sleep(3)
print()

print("Your final score is {}! Thank you for playing!".format(points))