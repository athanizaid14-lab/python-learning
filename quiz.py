print ("play a quiz and answer the following ques")


#Ques 1
j=["mumbai","delhi","bangalore","chennai"]
print ("which is the capital of india?")
print ("your options are:")
print ("1:" ,j[0],"\n" "2:",j[1], "\n" "3:",j[2], "\n" "4:",j[3])
print ("your answer?")

option = input()
option =option.lower()
score = 0
if option==j[1]:
    score = score + 1
    print("good")
else :
    print ("wrong")

print ("\n")
#Ques2  Which planet is known as the Red Planet?
#A) Earth
#B) Mars
#C) Jupiter

i=1
print ("Ques 2 : Which planet is known as the Red Planet?")
k=["earth","mars","jupiter"]
print ("your options are")
for ele in k:
    print (i,ele)
    i+=1
print ("your answer?")
ans=input()
ans=ans.lower()
if ans == k[1]:
    print ("correct")
    i+=1
    score = score + 1
else :
    print ("wrong")
    

print ("\n")
#What does len() do in Python?
#A) Finds length
#B) Deletes something
#C) Sorts something

print ("ques 3 :  What does len() do in Python?")
print ("your options are")
q3=["finds length","deletes something","sorts something"]
j=1
for ele in q3:
    print (j,ele)
    j+=1
print ()
print ("your answer?")
ans1=input()
ans1=ans1.lower()
if ans1==q3[0]:
    print ("correct")
    score = score + 1
else :
    print("wrong")

print ("your final score is = ", score)