import random
def shuffle(the_list):

    # Shuffle the input in place
    l = len(the_list)
    for i in range (l):
        r = random.randrange(i,l)
        if(r!=i):
            (the_list[i],the_list[r])=(the_list[r],the_list[i])
    


sample_list = [1, 2, 3, 4, 5]
print 'Sample list:', sample_list

print 'Shuffling sample list...'
shuffle(sample_list)
print sample_list
