name =input("Type your name : ")
print("Welcome", name, "to this adventure!")

answer= input ("You have come to a dirt road , it has come to an end.You can only go left and right.Which way would you like to go? ").lower()

if answer =="left":
  answer =input ("You have come to a river.You can walk around it or swim to swim across:Type walk or swim").lower()

  if answer == "swim":
    print("Hahahaha.You swam across and were esten by crocodiles")

  elif answer == "walk" :
    print("You walked for many miles,ran out of water.You lost !")

  else:
    print("Not a valid option you lose.")


 
elif answer == "right":
 answer= input("You come to a bridge, it looks wobbly,do you want to cross it or head back.Type cross or back").lower()  

 if answer == "cross":

    answer =input (" Phew ! You cross the bridge and meet a stranger.Do you talk to them?.Type yes or no").lower()
    if answer == "yes" :
      print("You talk to the stranger and they give you a ride out of the forest.YOU SURVIVE").lower()
    elif answer == "no":
      print("You ignore the stranger and walk away. Some few minutes later you are attacked by a lion.YOU DIE")
      
    else:
      print("Not a valid option.You lose.")

 elif answer == "back" :
    print("You go back you slip in on the bridge .You lose !")







else:
  print("Not a valid option.You lose.")
