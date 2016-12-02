from Task import Task
from Printer import Printer
from Queue import Queue
from random import randrange

def simulation(seconds, ppm):
    printQueue = Queue()
    waitingtimes = []
    printer = Printer(ppm)
    for currentSecond in range(seconds):
        if newPrintTask():
            printQueue.enqueue(Task("Task"+str(currentSecond), currentSecond))
        
        if (not printer.busy()) and (not printQueue.isEmpty()):
            nexttask = printQueue.dequeue()
            waitingtimes.append(nexttask.getWaitTime(currentSecond))
            printer.nextTask(nexttask)
        
        printer.tick()
    lenWaitTime = len(waitingtimes)
    averageWait=sum(waitingtimes)/lenWaitTime
    print("Average Wait %6.2f secs %3d tasks remaining."%(averageWait,printQueue.size()))

    

def newPrintTask():
    num = randrange(1,181)
    if num == 180:
        return True
    else:
        return False

for i in range(5):
    simulation(3600, 20)