import random
import time

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
        print("correct")
        points += 1
        counter += 1
      
      else:
        print("incorrect")
        counter += 1
    
    elif chosen2 == "a2":
      answer = input("bang for your ____ ").lower()
      if answer == "buck":
        print("correct")
        points += 1
        counter += 1
      
      else:
        print("incorrect")
        counter += 1
    
    elif chosen2 == "a3":
      answer = input("something _____ is going on ").lower()
      if answer == "fishy":
        print("correct")
        points += 1
        counter += 1
      
      else: 
        print("incorrect")
        counter += 1
    
    elif chosen2 == "a4":
      answer = input("hold your _______ ").lower()
      if answer == "horses":
        print("correct")
        points += 1
        counter += 1
      
      else:
        print("incorrect")
        counter += 1
    
    else:
      answer = input("______ again! ").lower()
      if answer == "foiled":
        print("correct")
        points += 1 
        counter += 1
      
      else:
        print("incorrect")
        counter += 1
  
  elif chosen == "b":
    questions = "b1", "b2", "b3", "b4", "b5"
    chosen2 = random.choice(questions)
    
    if chosen2 == "b1":
      answer = input("take a _____ pill ").lower()
      if answer == "chill":
        print("correct")
        points += 1
        counter += 1
     
      else:
        print("incorrect")
        counter += 1
    
    elif chosen2 == "b2":
      answer = input("every ___ has his day ").lower()
      if answer == "dog":
        print("correct")
        points += 1
        counter += 1

      else:
        print("incorrect")
        counter += 1

    elif chosen2 == "b3":
      answer = input("going the whole ____ yards ").lower()
      if answer == "nine":
        print("correct")
        points += 1
        counter += 1
  
      else: 
        print("incorrect")
        counter += 1
    
    elif chosen2 == "b4":
      answer = input("bob's your _____ ").lower()
      if answer == "uncle":
        print("correct")
        points += 1
        counter += 1 

      else:
        print("incorrect")
        counter += 1

    else:
      answer = input("feeling under the _______ ").lower()
      if answer == "weather":
        print("correct")
        points += 1 
        counter += 1
      
      else:
        print("incorrect")
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
        print("correct")
        points += 1
        counter += 1
      
      else:
        print("incorrect")
        counter += 1
    
    elif chosen2 == "c2":
      answer = input("giving the cold ________ ").lower()
      if answer == "shoulder":
        print("correct")
        points += 1
        counter += 1
      
      else:
        print("incorrect")
        counter += 1
    
    elif chosen2 == "c3":
      answer = input("spill the _____ ").lower()
      if answer == "beans":
        print("correct")
        points += 1
        counter += 1
      
      else: 
        print("incorrect")
        counter += 1
    
    elif chosen2 == "c4":
      answer = input("_____ doesn't grow on trees ").lower()
      if answer == "money":
        print("correct")
        points += 1
        counter += 1
      
      else:
        print("incorrect")
        counter += 1
    
    else:
      answer = input("better ____ than ever ").lower()
      if answer == "late":
        print("correct")
        points += 1 
        counter += 1
      
      else:
        print("incorrect")
        counter += 1

  if counter == 9:
    valid = True

print("your final score is {} out of 12!".format(points))