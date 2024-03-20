from random import random
a=int(random()*1000)
t=0
q=int(input("guess : "))
while q!=a :
    if a<q : print ("lower")
    else : print ("higher")
    q=int(input("guess : "))
    t+=1
print("CORRECT")
print("guesses : " +str(t))
k=int(input())