import random
comp=["rock","paper","scissor"]
ran=random.choice(comp)
while True:
    print ("enter your play")
    j=input()
    j=j.lower()

    if ran==j:
        print ("tie")
        break
    elif ran=="rock" and j=="paper":
        print ("I win")
        break
    elif ran=="paper" and j=="rock":
        print ("YOu win")
        break
    elif ran=="paper" and j=="scissor":
        print ("You win")
        break
    elif ran=="scisscor" and j=="paper":
        print ("I win")
        break
    elif ran=="scissor" and j=="rock":
        print ("You win")
        break
    elif ran=="rock" and j=="scissor":
        print ("I win")
        break
    else :
        print ("wrong input")
print("my input was", ran)   
