name =input("Type your name : ")
print("Welcome", name, "to this adventure!")

answer= input ("You have come to a dirt road , it has come to an end.You can only go left and right.Which way would you like to go? ").lower()

if answer =="left":
  answer =input ("You have come to a river.You can walk around it or swim to swim across:Type walk or swim").lower()

  if answer == "swim":
    print()

  elif answer == "walk" :
    print()

  else:
    print("Not a valid option you lose.")




  

 
elif answer == "right":
 print()
else:
  print("Not a valid option.You lose.")
