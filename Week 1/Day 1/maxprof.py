inp = eval(raw_input('enter input:'))
l = len(inp)
if(l<3):
    print 'Insufficient length'
else:
    max1 = inp[0]
    max2 = inp[1]
    max3 = inp[2]
    nmax1 = 0
    nmax2 = 0
    for x in inp:
        if(x<0):
            if(x<nmax1):
                nmax1=x
            elif(x<nmax2):
                nmax2=x
        if(x>max1):
            max3 = max2
            max2 = max1
            max1 = x
        elif(x>max2):
            max3 = max2
            max2 = x
        elif(x>max3):
            max3 = x
print 'maximum product:',max(max1*max2*max3,nmax1*nmax2*max1)
