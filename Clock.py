import time 
class Clock:
    def __init__(self):
        self.startTIme = time.time()
    
    


    def reset(self):
        self.startTIme = time.time()


    def getTimeElasped(self):
        return int(time.time() - self.startTIme)