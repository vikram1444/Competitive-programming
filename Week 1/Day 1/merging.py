class Meeting():
    def __init__(self,startTime,endTime):
        self.startTime = startTime
        self.endTime = endTime
    def getStartTime():
        return self.startTime
    def getEndTime():
        return self.endTime
def makeMeeting(i):
    m = Meeting(i[0],i[1])
    return m
inp = eval(raw_input('Enter meeting slots:'))
l = len(inp)
slots = map(makeMeeting,inp)
startTimes = []
endTimes = []
for slot in slots:
    startTimes.append(slot.startTime)
    endTimes.append(slot.endTime)
startTimes.sort()
endTimes.sort()
result = []
st = startTimes[0]
et = endTimes[0]
for i in range(l-1):
    if(startTimes[i+1]>endTimes[i]):
        result.append(Meeting(st,et))
        st = startTimes[i+1]
        et = endTimes[i+1]
    else:
        et = endTimes[i+1]
result.append(Meeting(st,et))
for res in result:
print '(',res.startTime,',',res.endTime,')'
