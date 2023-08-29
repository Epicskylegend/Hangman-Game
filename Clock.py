import time 
class Clock:
    def __init__(self):
        self.startTIme = time.time()
        self.timePerKey = time.time()
    
    


    def reset(self):
        self.startTIme = time.time()


    def resetTimePerKey(self):
        self.timePerKey = time.time()

    def getTimePerKey(self):
        return int(time.time() - self.timePerKey)


    def getTimeElasped(self):
        return int(time.time() - self.startTIme)