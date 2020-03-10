# Brynjolf problem
import sys
import gc
from room import Room
from brynjolf import Brynjolf
from establishment import establishment
from enlightenment import enlightenment

try:
    filePath = sys.argv[1]
except IndexError:
    filePath = input("Please enter a file name with the room: ")
    if not filePath:
        print ("No file provided. Using the defined Sample room.txt")
        filePath = 'room.txt'

r = Room(filePath)
(x, y) = r.brynjolf
b = Brynjolf(r.room, r.brynjolf, r.guards, r.exit)

solution = b.solution


# initially the room
def print_room():
    print ("Room:")
    for m in r.room:
        print (m)


room = b.room

approaches = {1: (establishment, "Establishment"), 2: (enlightenment, "Enlightenment")}

run = True
while run:
    print_room()
    try:
        choices = list(
            map(
                int, input(
                    "Do you want to: \n\
                    (1) Run Establishment \n\
                    (2) Run Enlightenment\n\
                    Or you can exit by typing 0\n").split()
            )
        )
    except ValueError:
        print ("Please Enter a Number of mentioned choices")
        continue
    for choice in choices:
        if choice == 0:
            run = False
            print ("Quit!")
        else:
            if 0 < choice and choice < 3:
                print("\n%d. %s it is then\n" % (choice, approaches[choice][1]))
                approaches[choice][0](b)
                run = False
            else:
                print ("That is not neither 1 nor 2! Try again:")

gc.collect()
