import random


def rand5():
    return random.randint(1, 5)


def rand7():
    # Implement rand7() using rand5()
    k = 5*rand5()+rand5()-5
    if(k<22):
        return k%7 + 1
    return rand7()


print 'Rolling 7-sided die...'
print rand7()
