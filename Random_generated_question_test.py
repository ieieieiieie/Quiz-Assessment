import random

questions = ("q1", "q2", "q3")

valid = False
while not valid:
      chosen = random.choice (questions)
  
      if chosen == "q1":
        q1 = input("what is cheese? ").lower()
        answer = "good" 
        
        if q1 == answer:
          print("correct")
          valid = True
        
        else:
          print("incorrect")
          valid = True
  
      if chosen == "q2":
        q1 = input("what is egg? ").lower()
        answer = "good" 
      
        if q1 == answer:
          print("correct")
          valid = True

        else:
          print("incorrect")
          valid = True
  
      if chosen == "q3":
        q1 = input("what is milk? ").lower()
        answer = "good" 
      
        if q1 == answer:
          print("correct")
          valid = True
        
        else:
          print("incorrect")
          valid = True