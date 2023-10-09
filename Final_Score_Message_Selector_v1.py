points = 12 #messages are tested for the different variables and they work correctly

if points == 0:
  print("0 point message")

elif points <6: 
  print("1 - 5 point message")

elif points == 6:
  print("6 point message")

elif points <12:
  print("7 - 11 point message")

else:
  print("12 point message")

print()
print("points = {}".format(points))