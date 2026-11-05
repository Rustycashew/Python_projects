import random
number = random.randint(1,100)
attempts = 7
attempt = 0
print("Welcome to the Number Guessing Game")
print("I have a selected a number between 1 and 100")
print("You have 7 guesses to guess the number.\n")
while True:
    if (attempt>attempts):
        print("\n Game Over!!")
        print("The correct number was: " , number)
    guess = int(input("Enter your number: "))
    attempt += 1
    if(0>guess or guess>100):
        print("Please enter a number between 1 and 100 , try again")
    if (guess<number):
        print("Too low!!! , try again")
    elif(guess>number):
        print("Too high!!!, try again")
    else:
        print("Congratulations!!!, You guessed the number")
        print("The number was: ", number)
        print("Attempts taken: ", attempt)
        break            
                
    
    
    