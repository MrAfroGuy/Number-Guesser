import random
import math
def guessgame():
    #Random Number
    randnum = random.randint(1,500)
    guess = input
    
    while guess != randnum:
    #guess
        guess = int(input('Enter a Guess: '))
        if guess == randnum:
            print('Congrats you have guessed the number')
        else:
            print('Not Correct,Try Again')
            if guess > randnum:
                print('Number is too High')
            else:
                print('Number is too low')
        
            
guessgame()    
    
    
    
    