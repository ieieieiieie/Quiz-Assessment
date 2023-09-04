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
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Its time to ramp things up! Have you gotten used to the quiz yet?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)

print("from this point forward, all the questions will be random!")
time.sleep(2)
print()
print("Get ready!")

pools = "a", "b", "c", "d" 
counter = 0

valid = False
while not valid:
  chosen = random.choice(pools)
  time.sleep(3)
  print()
  
  if chosen == "a":
    questions = "a1", "a2", "a3", "a4", "a5"
    chosen2 = random.choice(questions)
  
    if chosen2 == "a1":
      answer = input("piece of ____ ").lower()
      if answer == "cake":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was cake!")
        counter += 1
    
    elif chosen2 == "a2":
      answer = input("bang for your ____ ").lower()
      if answer == "buck":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer is buck!")
        counter += 1
    
    elif chosen2 == "a3":
      answer = input("something _____ is going on ").lower()
      if answer == "fishy":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
      
      else: 
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer is fishy!")
        counter += 1
    
    elif chosen2 == "a4":
      answer = input("hold your _______ ").lower()
      if answer == "horses":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was horses!")
        counter += 1
    
    else:
      answer = input("curses! ______ again! ").lower()
      if answer == "foiled":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1 
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was foiled!")
        counter += 1
  
  elif chosen == "b":
    questions = "b1", "b2", "b3", "b4", "b5"
    chosen2 = random.choice(questions)
    
    if chosen2 == "b1":
      answer = input("take a _____ pill ").lower()
      if answer == "chill":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
     
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was chill!")
        counter += 1
    
    elif chosen2 == "b2":
      answer = input("every ___ has his day ").lower()
      if answer == "dog":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1

      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer is dog!")
        counter += 1

    elif chosen2 == "b3":
      answer = input("going the whole ____ yards ").lower()
      if answer == "nine":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point")
        points += 1
        counter += 1
  
      else: 
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was 9!")
        counter += 1
    
    elif chosen2 == "b4":
      answer = input("bob's your _____ ").lower()
      if answer == "uncle":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1 

      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was uncle!")
        counter += 1

    else:
      answer = input("feeling under the _______ ").lower()
      if answer == "weather":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1 
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was weather!")
        counter += 1 

  elif chosen == "c":
    questions = "c1", "c2", "c3", "c4", "c5"
    chosen2 = random.choice(questions)
    
    if chosen2 == "c1":
      answer = input("a dime a _____ ").lower()
      if answer == "dozen":
        print("correct")
        points += 1
        counter += 1
     
      else:
        print("incorrect")
        counter += 1
    
    elif chosen2 == "c2":
      answer = input("_________ killed the cat ").lower()
      if answer == "curiosity":
        print("correct")
        points += 1
        counter += 1

      else:
        print("incorrect")
        counter += 1

    elif chosen2 == "c3":
      answer = input("jumping at _______ ").lower()
      if answer == "shadows":
        print("correct")
        points += 1
        counter += 1
  
      else: 
        print("incorrect")
        counter += 1
    
    elif chosen2 == "c4":
      answer = input("cut and ___ ").lower()
      if answer == "dry":
        print("correct")
        points += 1
        counter += 1 

      else:
        print("incorrect")
        counter += 1

    else:
      answer = input("over the ____ ").lower()
      if answer == "moon":
        print("correct")
        points += 1 
        counter += 1
      
      else:
        print("incorrect")
        counter += 1 

  else:
    questions = "c1", "c2", "c3", "c4", "c5"
    chosen2 = random.choice(questions)
    
    if chosen2 == "c1":
      answer = input("needle in a _______ ").lower()
      if answer == "haystack":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was haystack!")
        counter += 1
    
    elif chosen2 == "c2":
      answer = input("giving the cold ________ ").lower()
      if answer == "shoulder":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point")
        points += 1
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was shoulder!")
        counter += 1
    
    elif chosen2 == "c3":
      answer = input("spill the _____ ").lower()
      if answer == "beans":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point")
        points += 1
        counter += 1
      
      else: 
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was beans!")
        counter += 1
    
    elif chosen2 == "c4":
      answer = input("_____ doesn't grow on trees ").lower()
      if answer == "money":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! the correct answer was money!")
        counter += 1
    
    else:
      answer = input("better ____ than ever ").lower()
      if answer == "late":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1 
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer was late!")
        counter += 1

  if counter == 9:
    valid = True

print("your final score is {} out of 12!".format(points))