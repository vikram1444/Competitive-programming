inp = eval(raw_input('enter input:'))
l = len(inp)
if(l<2):
    print('Insufficient length')
else:
    product = 1
    prodArray = []
    for x in inp:
        prodArray.append(product)
        product = product * x
    product = 1
    for x in range(l-1,-1,-1):
        prodArray[x] = prodArray[x]*product
        product = product*inp[x]
print 'resultant list:',prodArray
