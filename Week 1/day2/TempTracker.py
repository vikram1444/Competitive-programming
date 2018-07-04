class TempTracker(object):
    
    def __init__(self):
        self.maxtimes=0
        self.mode=0
        self.occurances = [0 for i in range (110)]
        
        self.maxtemp=None
        self.mintemp=None
        
        self.numoftemp=0
        self.sumoftemp=0
    

    def insert(self, temperature):
        if(self.maxtemp==None):
           self.mintemp=temperature
           self.maxtemp=temperature
        else:
            if(temperature<self.mintemp):
                self.mintemp=temperature
            elif(temperature>self.maxtemp):
                self.maxtemp=temperature
        x = self.occurances[temperature]+1
        self.occurances[temperature] = x
        if(x>self.maxtimes):
            self.maxtimes = x
            self.mode = temperature
        self.sumoftemp = self.sumoftemp + temperature
        self.numoftemp = self.numoftemp + 1

    def get_max(self):
        return self.maxtemp

    def get_min(self):
        return self.mintemp

    def get_mean(self):
        return float(self.sumoftemp/self.numoftemp)

    def get_mode(self):
        return self.mode
temp = TempTracker()
temp.insert(50)
temp.insert(100)
temp.insert(50)
temp.insert(60)
print 'min:',temp.get_min()
print 'max:',temp.get_max()
print 'mean:',temp.get_mean()
print 'mode:',temp.get_mode()
