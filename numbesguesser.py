import random
j= random.randint(1,5)


while True:
    print ("enter your guess")
    i=int(input())
    if i==j:
        print ("correct")
        guess=True
        break
    elif i<=j%2:
        print ("your guess is lower")
        
    elif i>=j%2:
        print ("your guess is too high")
        
    elif i==j%2:
        print ("your guess in in between") 
   