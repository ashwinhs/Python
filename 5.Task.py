from random import randrange

class Task:
    def __init__(self, name, time):
        self.name = name
        self.time = time
        self.pages = randrange(1,21)
    
    def getWaitTime(self, currentTime):
        return currentTime - self.time
    
    def getName(self):
        return self.name
    
    def getPages(self):
        return self.pages