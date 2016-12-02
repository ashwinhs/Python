class Printer:
    def __init__(self, ppm):
        self.ppm = ppm
        self.task = None
        self.timeRemaining = 0
    
    def tick(self):
        if self.timeRemaining > 0:
            self.timeRemaining -= 1
        else:
            self.task = None
    
    def busy(self):
        if self.timeRemaining == 0 or self.task == None:
            return False
        else:
            return True
    
    def nextTask(self, task):
        self.task = task
        self.timeRemaining = self.task.getPages() * 60/self.ppm
        
        