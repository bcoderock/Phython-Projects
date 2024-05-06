print("Welcome to my computer quiz!")

playing = input("Do you want to play? ")

if playing.lower() != "yes" :
    quit()

print("Okay!Lets play dear ")

score=0
questions= 0

answer = input("What does CPU stand for? ")
questions +=1
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does RAM stand for? ")
questions +=1
if answer.lower() == "random access memory":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does GPU stand for? ")
questions +=1
if answer.lower() == "graphics processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does CPU stand for? ")
questions +=1
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

answer = input("What does CPU stand for? ")
questions +=1
if answer.lower() == "central processing unit":
    print("Correct")
    score += 1
else:
    print("Incorrect")

print ("Your had " + str(questions)+" questions") 
print("Your score is " + str(score)+ " questions correct") 
print("Your percentage is " + str(score/questions*100) + "%") 

