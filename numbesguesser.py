#number guessing from 1 to 10

import random
j= random.randint(1,10)


while True:
    print ("enter your guess")
    i=int(input())
    if i==j:
        print ("your guess is correct")
        
        break
    elif i<=j%2:
        print ("your guess is low, the value is bit higher")
        
    elif i>=j%2:
        print ("your guess is too high")
        
    elif i==j%2:
        print ("your guess is in between") 

