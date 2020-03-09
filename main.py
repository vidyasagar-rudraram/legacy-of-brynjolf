# Brynjolf problem
import sys
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
print ("brynjolf at: "), b.brynjolf
print ("guards at: "), b.guards
print ("exit at: "), b.exit
solution = b.solution
steps = b.steps
sol_path = b.sol_path


# initially the room
def print_room():
    print ("Room:")
    for m in r.room:
        print (m)


def print_solution():
    print ("Solution:")
    for s in solution:
        print (s)


room = b.room

approaches = {1: establishment, 2: enlightenment}

run = True
while run:
    print ("\n-----------------------------------------")
    print_room()
    print ()
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
                approaches[choice](b)
                run = False
            else:
                print ("That is not neither 1 nor 2! Try again:")
