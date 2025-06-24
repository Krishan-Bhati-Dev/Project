import random
import datetime
print("~~~~~~~ Hey! Welcome ~~~~~~~")

#assign user and comp and tie score is 0
user_score = 0
comp_score = 0
tie = 0

#input user name 
user_name = input("Enter your name:")
print()
print(f"Welcome!, {user_name}")

#game rule
print("Let's get familier with winning Rules: ")
print(''' 
        Rock and Paper --> Paper
        Paper and Scissor --> Scissor
        Rock and Paper --> Rock
    ''')

while True:
    print('''Choices are:
    1 -> Paper
    2 -> Scissor
    3 -> Rock
    ''')
    
    # print and input choice for r,s,p
    user_choice = int(input("Enter your choice:"))
    print()
        
    while user_choice>3 or user_choice<1:  # Validating input
        user_choice = int(input("enter valid choice"))
    
    if (user_choice==1):
        user_choice = "Paper"
    elif(user_choice==2):
        user_choice= "Scissor"
    else:
        user_choice= "Rock"
    print("Your choice is",user_choice)
   
    # now computer's ramdom turn and print computer choice
    computer = random.randint(1,3)
    if (computer==1):
        comp_choice = "Paper"
    elif(computer==2):
        comp_choice ="Scissor"
    else:
        comp_choice = "Rock"
    
    print("The computer's choice is", comp_choice)
    
    #condition for winning
    if((user_choice=="Paper" and comp_choice=="Rock") or (user_choice=="Rock" and comp_choice=="Paper")):
        result = "Paper"
    elif((user_choice=="Scissor" and comp_choice=="Rock") or (user_choice=="Rock" and comp_choice=="Scissor")):        
        result= "Rock"
    elif(user_choice == comp_choice):        
        result = "Tie"
    else:        
        result = "Scissor"

    # now score increment
    if (result== "Tie"):
        tie+=1
    elif(result==user_choice):        
        user_score +=1
    else:       
        comp_score+=1
    
    print()

    # Print scores
    print(f"{user_name}'s score is {user_score}")
    print("computer's score is",comp_score)
    print("ties are:",tie)  
    print()
    

    # Asking user whether to play again
    again = input("Do you want to play the game again? --> press yes or no:")
    if (again.lower()== "no"):
        break
print()
# who won the game
if(user_score>comp_score):
    print(f"{user_name}, You won the game!")
elif(comp_score>user_score):
    print("You lost!, Better luck next time🤞")
else:
    print("Nobody won!")

# Stores the history of the game in a file
now = datetime.datetime.now()
format = now.strftime("%d-%m-%Y %H:%M:%S")

with open("C:/Users/KRISHAN BHATI/OneDrive/Desktop/python/Files_exam/python_project/score.txt","a") as f:
    f.write(f"{format}\n")
    f.write(f"{user_name} score is {user_score} \ncomputer's score is {comp_score}\nties are {tie}\n\n")
    
print("Hope you enjoy the game and Thanks for Playing!!") 