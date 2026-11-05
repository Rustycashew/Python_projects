import random
computer = random.choice([-1,0,1])
youstr = input("Enter your choice: ")
youDict = {"p":1 , "r": -1 , "s": 0}
reverseDict = {1: "Paper" , -1: "Rock" , 0: "Scissors"}
you = youDict[youstr]


print(f"You Chose : {reverseDict[you]} \nComputer Chose: {reverseDict[computer]}")

if(computer == you):
    print("It's a draw")
    
else: 
        
    if(computer == -1 and you == 1):
        print("You win!")

    elif(computer == -1 and you == 0):
        print("You lose!")

    elif(computer == 1 and you == -1):
        print("You lose!")

    elif(computer == 1 and you == 0):
        print("You win!")
        
    elif(computer == 0 and you == -1):
        print("You win!")    
    elif(computer == 0 and you == 1):
        print("You lose!")       
    else:
        print("Something went wrong")    