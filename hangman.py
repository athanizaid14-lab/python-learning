import random
words = ["python","github","java", "git", "pyranos"]
word=random.choice(words)

i=[]
for letter in word:
   i.append(letter)
k=0
while True:
    print ("first letter guess is :", end =" ")
    g1=input()
    if g1==i[0]:
      print ("correct guess now enter guess 2")
      k+=0
    else :
      break



    print ("second letter guess is", end="")
    g2=input()
    if g2==i[1]:
      print ("correct guess now enter guess 3")
      k+=0
    else :
      break


    print ("third letter guess is", end="")
    g3=input()
    if g3==i[2]:
        print ("correct guess now enter guess 4")
        k+=1
    elif k==len(i):
       break
    else :
       break


    print ("fourth letter guess is", end="")
    g4=input()
    if g4==i[3]:
        print ("correct guess now enter guess 5")
        k+=1
    elif k==len(i):
       break
    else :
       break



    print ("fifth letter guess is", end="")
    g5=input()
    if g5==i[4]:
        print ("correct guess now enter guess 6 ")
        k+=1
    elif k==len(i):
       break
    else :
       break



    print ("six letter guess is", end="")
    g6=input()
    if g6==i[5]:
        print ("correct guess now enter guess 7")
        k+=1
    elif k==len(i):
       break
    else :
       break
 


    print ("seventh letter guess is", end="")
    g4=input()
    if g4==i[6]:
        print ("your word is right")
    else:
       print ("you lost at the last letter, sheesh")
       break

print ("the word is", i)