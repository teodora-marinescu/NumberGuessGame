from random import random

# generates random number
a=int(random()*1000)
# number of tries is set to 0
t=0
# q is the number you guess
q=int(input("guess : "))

# while your guess is wrong the number of tries increases 
while q!=a :
    if a<q : print ("lower")
    else : print ("higher")
    q=int(input("guess : "))
    t+=1

# when the guess is correct the message and number of tries are displayed
print("CORRECT")
print("guesses : ",t)
k=int(input())
