increment = 13
current = 14
lowerlimit = 1
iteration = 1
ip = input('enter floor number')
while(current!=ip):
    print 'cur',current
    if (current>ip):
        current = lowerlimit
        print 'iteration -',iteration
        while(current!=ip):      
            print 'cur',current
            print 'iteration -',iteration
            current+=1
            iteration+=1
    elif (current<ip):
        print 'iteration -',iteration
        iteration+=1
        lowerlimit+=increment+1
        current+=increment        
        increment-=1
print 'found the floor in',iteration,'iteration'
