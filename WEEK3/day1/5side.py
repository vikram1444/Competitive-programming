import random

def rand7():
    return random.randint(1, 7)

def rand5():

    # Implement rand5() using rand7()
    roll = rand7()
    return roll if roll <= 5 else rand5()
print 'Rolling 5-sided die...'
print rand5()
