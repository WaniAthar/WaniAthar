from random import randint
import os
while True:
    inp = input("Press 't' to toss: ")
    toss = randint(0,1)
    if inp == "t":
        if toss == 0:
            print("Head")
        elif toss == 1:
            print("Tail")
        else:
            pass
    else:
        print("Please enter the correct input")
   