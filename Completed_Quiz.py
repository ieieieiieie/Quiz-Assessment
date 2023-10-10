#time module to create pauses between prints

import random
import time


#function to get the player's name
def p_name(question):
  valid = False
  while not valid:
    player_name = input(question)

    if player_name.isalpha():
      valid = True
      return player_name

    else:
      print("{} is not a valid name".format(player_name))

#function to get the player's answer on displaying the introduction
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

#function for the introduction display
def introduction():
  print("~~~INTRODUCTION~~~")
  print()
  print("You will have to answer 12 questions")
  print()
  print("These questions will be famous human sayings to refer to something else")
  print()
  print("You will get a prompt for one of the sayings with a word missing in it")
  print()
  print("You have to try to guess what word this is")
  print("~~~~~~~~~~~~~~~~~~")
  return ""

#main routine

#response after successfully picking a valid name
player_name = p_name("Please enter your name (letters only) ")
time.sleep(2)
print("{} is a valid name, thank you for entering.".format(player_name))
print()

#code to display or to not display the instructions accordingly
answer = user_answer("would you like to see the introduction {}? ".format(player_name))
if answer == "yes":
  time.sleep(1)
  print()
  introduction()

#print statement to move to the next component
time.sleep(1)
print("Good luck on this quiz {}!".format(player_name))

#variable which tracks how many questions are marked as correct
points = 0 
time.sleep(5)

#question 1, the same structure is used for the first 3 questions
q1 = input("The ___ is out of the bag, what is the missing word? ").lower()

#if statement to check if the answer is correct
if q1 == "cat":
  points += 1 
  print("{}...".format(q1))
  time.sleep(3)
  print("is the correct answer! +1 point!")

#else statement to display the correct answer if the question was incorrect
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

#display before the questions are randomly chosen from different pools
time.sleep(5)
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
print("Its time to ramp things up! Have you gotten used to the quiz yet?")
print("~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~~")
time.sleep(3)

print("from this point forward, all the questions will be random!")
time.sleep(2)
print()
print("Get ready!")

#the pool variables 
pools = "a", "b", "c", "d" 
#used to track how many questions have been answered
counter = 0

#this loop contains every possible question
valid = False
while not valid:
  #code to choose which pool is used for the question
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
        #the counter feature has been implemented here
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
      answer = input("hold your ______ ").lower()
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
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
     
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer is dozen!")
        counter += 1
    
    elif chosen2 == "c2":
      answer = input("_________ killed the cat ").lower()
      if answer == "curiosity":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1

      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! the correct answer is curiosity!")
        counter += 1

    elif chosen2 == "c3":
      answer = input("jumping at _______ ").lower()
      if answer == "shadows":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1
        counter += 1
  
      else: 
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! the correct answer is shadows!")
        counter += 1
    
    elif chosen2 == "c4":
      answer = input("cut and ___ ").lower()
      if answer == "dry":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point")
        points += 1
        counter += 1 

      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer is dry!")
        counter += 1

    else:
      answer = input("over the ____ ").lower()
      if answer == "moon":
        print("{}...".format(answer))
        time.sleep(3)
        print("is the correct answer! +1 point!")
        points += 1 
        counter += 1
      
      else:
        print("{}...".format(answer))
        time.sleep(3)
        print("is the incorrect answer! The correct answer is moon!")
        counter += 1 

  else:
    questions = "d1", "d2", "d3", "d4", "d5"
    chosen2 = random.choice(questions)
    
    if chosen2 == "d1":
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
    
    elif chosen2 == "d2":
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
    
    elif chosen2 == "d3":
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
    
    elif chosen2 == "d4":
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

  #code used to break the loop after 9 questions have been answered
  if counter == 9:
    valid = True

time.sleep(5)
print()

#0 point message display
if points == 0:
  print("oh dear! Better luck next time {}!".format(player_name))

#1 - 5 point message display
elif points <6: 
  print("Great try {}! You still have a long way to go!".format(player_name))

#6 point message display
elif points == 6:
  print("halfway there now {}. Almost there!".format(player_name))

#7 - 11 point message display
elif points <12:
  print("More than 50%! Great job {}!".format(player_name))

#12 point message display
else:
  print("Full marks! Excellent work {}!".format(player_name))

#code to display the final score
print()
print("points = {}".format(points))