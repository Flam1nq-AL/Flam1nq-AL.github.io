# Adrian Leung | Dulwich College | 16

#Question 1

def decrypt(word):
    mylist = []
    
    for i in range(len(word)):
        mylist.append(ord(word[i]) - 64)
    
    mylist.reverse()
    
    for i in range(len(mylist)-1):
        mylist[i] -= mylist[i+1]
        if mylist[i] < 0:
            mylist[i] += 26
    
    mylist.reverse()
    
    for i in range(len(mylist)):
        mylist[i] = chr(mylist[i] + 64)
    
    return(''.join(mylist))

def encrypt(word):
    mylist = []
    
    
    for i in range(len(word)):
        mylist.append(ord(word[i]) - 64)
    
    for i in range(1,len(mylist)):
        mylist[i] += mylist[i-1]
        if mylist[i] > 26:
            mylist[i] -= 26
    
    
    for i in range(len(mylist)):
        mylist[i] = chr(mylist[i] + 64)
    
    return(''.join(mylist))
    
    
print(encrypt('ZZZZZ'))

mystring = 'AAA'
for i in range(26*26):
    mystring = encrypt(mystring)

print(mystring)




#Question 2

def drones(red_jump,blue_jump,skirmishes,feuds):
    grid = [[0 for x in range(5)] for y in range(5)]
    print(grid) 