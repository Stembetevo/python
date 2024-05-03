print("Welcome to my quiz game!")

message = input("Do you want to play? ")
if message.lower() != "yes":
        quit()
else:
        print("Okay let's play!")
score = 0
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
        print("Correct!")
        score +=1
else:
        print("Incorrect!!")        
answer = input("What does CPU stand for? ")
if answer.lower() == "central processing unit":
        print("Correct!")
        score +=1
else:
        print("Incorrect!!")      

answer = input("What does TO stand for? ")
if answer.lower() == "training officer":
        print("Correct!")
        score +=1
else:
        print("Incorrect!!")

answer = input("What does RAM stand for? ")
if answer.lower() == "random access memory":
        print("Correct!")
        score +=1
else:
        print("Incorrect!!")     

print("\n""You have " + str(score) + " correct answers") 