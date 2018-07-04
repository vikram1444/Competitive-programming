deno = eval(raw_input('denominations:'))
amount = eval(raw_input('amount:'))
l = len(deno)
result = [[0 for i in range(l)] for j in range(amount+1)]
for x in range(l):
    result[0][x] = 1
for i in range(1,amount+1):
    for j in range(l):
            x = result[i - deno[j]][j] if i-deno[j] >= 0 else 0
            y = result[i][j-1] if j >= 1 else 0
            result[i][j]=x+y
        
            
print 'number of possible ways:',result[amount][l-1]
