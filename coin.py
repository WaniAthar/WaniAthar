from random import randint
import os
import datetime
from time import sleep


def stop():
    for i in range(7):
        print("Head")
        sleep(0.15)
        os.system("cls")
        print("Tail")
        sleep(0.15)
        os.system("cls")
        


while True:
    inp = input("Press 't' to toss: ")
    toss = randint(0, 1)
    
    if inp == "t":
        stop()
        if toss == 0:
            print("Head")
        elif toss == 1:
            print("Tail")
        else:
            pass
    else:
        print("Please enter the correct input")
