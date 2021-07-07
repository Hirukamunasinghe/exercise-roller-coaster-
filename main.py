height = int(input("What is your height?"))
if height > 120:
  print("You can ride the roller coaster")
  age = int(input("What is your age?"))
  if age <12 :
    print("You should pay $5.")
  elif age <=18 : 
    print ("You should pay $7.")
  else : 
    print ("You should pay $12.")
else :
    print ("sorry, you should grow taller before you ride")
