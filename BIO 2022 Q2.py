# Adrian Leung | Dulwich College | 16

#Question 2

class hexagon:
    
    def __init__(self):
        self.s1 = '-'
        self.s2 = '-'
        self.s3 = '-'
        self.s4 = '-'
        self.s5 = '-'
        self.s6 = '-'
    
    def change_colour(self,side,colour):
        if side == 1:
            if colour == 'Red':
                self.s1 = 0
            else:
                self.s1 = 1
        elif side == 2:
            if colour == 'Red':
                self.s2 = 0
            else:
                self.s2 = 1
        elif side == 3:
            if colour == 'Red':
                self.s3 = 0
            else:
                self.s3 = 1
        elif side == 4:
            if colour == 'Red':
                self.s4 = 0
            else:
                self.s4 = 1
        elif side == 5:
            if colour == 'Red':
                self.s5 = 0
            else:
                self.s5 = 1
        elif side == 6:
            if colour == 'Red':
                self.s6 = 0
            else:
                self.s6 = 1
    
    def display(self):
        edges = []
        edges.append(self.s1)
        edges.append(self.s2)
        edges.append(self.s3)
        edges.append(self.s4)
        edges.append(self.s5)
        edges.append(self.s6)
        print(edges)
    
    def owner(self):
        edges = []
        edges.append(self.s1)
        edges.append(self.s2)
        edges.append(self.s3)
        edges.append(self.s4)
        edges.append(self.s5)
        edges.append(self.s6)
        if edges.count(0) > edges.count(1):
            return 'Red'
        elif edges.count(1) > edges.count(0):
            return 'Blue'
        elif edges.count(1) > 0:                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                                            
            return 'Draw'
        else:
            return 'None'
        
            

def drones(red_jump,blue_jump,skirmishes,feuds):
    grid = [[hexagon() for x in range(5)] for y in range(5)]
    print(grid)
    if skirmishes > 0:
        grid[0][0].change_colour(1,'Red')
        grid[4][4].change_colour(6,'Blue')
        grid[3][3].change_colour(3,'Blue')
        skirmishes -= 1
    redrow = 0
    redcol = 0
    bluerow = 4
    bluecol = 4
    red_side = 1
    blue_side = 6
    for i in range(skirmishes):
        redrow += red_jump // 5
        redcol += red_jump % 5
        if redcol > 4:
            redcol -= 5
            redrow += 1
        if redrow > 4:
            redrow -= 5
        red_side += 1
        if red_side > 6:
            red_side -= 6
        grid[redrow][redcol].change_colour(red_side,'Red')
        if red_side == 2 and redcol < 4:
            grid[redrow][redcol+1].change_colour(5,'Red')
        elif red_side == 5 and redcol > 0:
            grid[redrow][redcol+1].change_colour(2,'Red')
        elif red_side == 1 and redrow != 0 and not(redrow == 1 and redcol == 4) and not(redrow == 3 and redcol == 4):
            if redrow == 2 or redrow == 4:
                grid[redrow-1][redcol].change_colour(4,'Red')
            else:
                grid[redrow-1][redcol+1].change_colour(4,'Red')
        elif red_side == 4 and redrow != 4 and not(redrow == 0 and redcol == 0) and not(redrow == 2 and redcol == 0):
            if redrow == 1 or redrow == 3:
                grid[redrow+1][redcol].change_colour(1,'Red')
            else:
                grid[redrow+1][redcol-1].change_colour(1,'Red')
        elif red_side == 3 and redrow != 4 and not(redrow == 1 and redcol == 4) and not(redrow == 3 and redcol == 4):
            if redrow == 2 or redrow == 0:
                grid[redrow+1][redcol].change_colour(6,'Red')
            else:
                grid[redrow+1][redcol+1].change_colour(6,'Red')
        elif red_side == 6 and redrow != 0 and not(redrow == 0 and redcol == 2) and not(redrow == 0 and redcol == 4):
            if redrow == 1 or redrow == 3:
                grid[redrow-1][redcol].change_colour(3,'Red')
            else:
                grid[redrow-1][redcol-1].change_colour(3,"Red")
        
        
        bluerow += blue_jump // 5
        bluecol += blue_jump % 5
        if bluecol > 4:
            bluecol -= 5
            bluerow += 1
        if bluerow > 4:
            bluerow -= 5
        blue_side += 1
        if blue_side > 6:
            blue_side -= 6
        print(bluerow,bluecol)
        grid[bluerow][bluecol].change_colour(blue_side,'Blue')
        if blue_side == 2 and bluecol < 4:
            grid[bluerow][bluecol+1].change_colour(5,'Blue')
        elif blue_side == 5 and bluecol > 0:
            grid[bluerow][bluecol+1].change_colour(2,'Blue')
        elif blue_side == 1 and bluerow != 0 and not(bluerow == 1 and bluecol == 4) and not(bluerow == 3 and bluecol == 4):
            if bluerow == 2 or bluerow == 4:
                grid[bluerow-1][bluecol].change_colour(4,'Blue')
            else:
                grid[bluerow-1][bluecol+1].change_colour(4,'Blue')
        elif blue_side == 4 and bluerow != 4 and not(bluerow == 0 and bluecol == 0) and not(bluerow == 2 and bluecol == 0):
            if bluerow == 1 or bluerow == 3:
                grid[bluerow+1][bluecol].change_colour(1,'Blue')
            else:
                grid[bluerow+1][bluecol-1].change_colour(1,'Blue')
        elif blue_side == 3 and bluerow != 4 and not(bluerow == 1 and bluecol == 4) and not(bluerow == 3 and bluecol == 4):
            if bluerow == 2 or bluerow == 0:
                grid[bluerow+1][bluecol].change_colour(6,'Blue')
            else:
                grid[bluerow+1][bluecol+1].change_colour(6,'Blue')
        elif blue_side == 6 and bluerow != 0 and not(bluerow == 0 and bluecol == 2) and not(bluerow == 0 and bluecol == 4):
            if bluerow == 1 or bluerow == 3:
                grid[bluerow-1][bluecol].change_colour(3,'Blue')
            else:
                grid[bluerow-1][bluecol-1].change_colour(3,'Blue')

    for i in range(feuds):
        pass
    
    redcount = 0
    bluecount = 0
    
    for i in grid:
        for x in i:
            x.display()
            if x.owner() == 'Red':
                redcount += 1
            elif x.owner() == 'Blue':
                bluecount += 1
    
    print(redcount,bluecount)
                
    
        
    

drones(9,3,3,1) 