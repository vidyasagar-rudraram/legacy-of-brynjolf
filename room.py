import os
import json
import sys
from util import find_character_index


class Room:

    def __init__(self, filePath):
        while not os.path.exists(filePath):
            filePath = raw_input("File doesn't exist in the path. Please try again with another file name: ")
        room = []

        with open(filePath) as textFile:
            for i, line in enumerate(json.load(textFile)):
                room.append(line)

        self.room = room
        self.brynjolf = (self.x, self.y) = self.getBrynjolf()
        self.guards = self.getGuards()
        self.exit = (self.ex, self.ey) = self.getExit()

    def printRoomBluePrint(self):
        for row in self.room:
            print (row)

    def getBrynjolf(self):
        brynjolf = find_character_index(self.room, "B")
        if len(brynjolf) > 0:
            return brynjolf[0]
        print "Brynjolf was not in the Room"
        sys.exit()

    def getGuards(self):
        guards = find_character_index(self.room, "G")
        return guards

    def getExit(self):
        exit = find_character_index(self.room, "E")
        if len(exit) > 0:
            return exit[0]
        print "There is no exit exist in the Room"
        sys.exit()
