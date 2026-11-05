import random
name = input("Enter your name: ")
print("Good Luck!!!" , name)

words = ['football' , 'ball', 'saxophone', 'disc' , 'messi' , 'flowers', 'keyboard' , 'mediocre' , 'record' , 'mother', 'mall', 'mail' , 'mouse']
word = random.choice(words)

print("\nGuess the Charecters")
guesses = ''
turns = 11
while turns > 0:
    
    failed = 0
    
    for char in word:
        if char in guesses:
            print(char,end = "")
        else:
            print("_" , end = "")
            failed += 1
    print()                
    if(failed == 0):
        print("You Win!!")
        print("The Word is: " , word)
        break
    guess = input("Enter your guess: ")
    if len(guess) !=1:
        print("Please enter a single charecter")
        continue
    if guess in guesses:
        print("You already guessed the charecter")    
        continue
    guesses += guess
    if guess not in word:
     turns -= 1
    print("Wrong")
    print("You have", +turns,'more guesses' )
    
    if (turns==0):
        print("You lose!")    
        print("The word was :" , word)    
    
     

                 
            
