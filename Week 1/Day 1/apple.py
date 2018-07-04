inp = eval(raw_input('enter input:'))
l = len(inp)
if (l<2):
    print 'insufficient input'
else:
    min = inp[0]
    diff = inp[1]-inp[0]
    for i in range(1,l):
        x = inp[i]
        if(x-min > diff):
            diff = x-min
        if(x<min):
            min = x
print 'maximum profit:',diff
