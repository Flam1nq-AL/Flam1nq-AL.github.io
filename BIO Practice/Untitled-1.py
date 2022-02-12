def palindromes (num):
    found = False
    while found == False:
        num += 1
        if str(num) == str(num)[::-1]:
            found = True
        print(num)
    return num

def rgbtriangle(row):
    nextrow = ''
    done = False
    if len(row) == 1:
        return row
    while done == False:
        for i in range(len(row)-1):
            if row[i] == row[i+1]:
                nextrow += row[i]
            else:
                if 'R' not in [row[i],row[i+1]]:
                    nextrow += 'R'
                if 'G' not in [row[i],row[i+1]]:
                    nextrow += 'G'
                if 'B' not in [row[i],row[i+1]]:
                    nextrow += 'B'
        row = nextrow
        if len(row) == 1:
            done = True
        nextrow = ''
    return row

print(rgbtriangle('GRBRBRBRBR'))

def dotsandboxes (p1,m1,p2,m2,moves):
    
    class Node:
        def __init__(self,data):
            self.data = data
            self.left = None
            self.right = None
            self.up = None
            self.down = None
        
    
    def check_box():
        pass
    
    grid = [['*' for a in range(5)] for b in range(5)]
    for i in range(moves):
        pass

def mysteryparcel(numParcels,maxWeight,numItems,parcelWeight):
    pass

def passwords(password):
    patterns = []
    for i in range(len(password)):
        patterns.append(password[:i+1])
    print(patterns)
    passwordcopy = password
    for pattern in patterns:
        print(pattern)
        if pattern in password:
            password = password.replace(pattern,'',1)
            print(password)
        if pattern in password:
            return False
        password = passwordcopy
        print(password)
    return True
        

print(passwords('hello'))





        
        
        
        
                