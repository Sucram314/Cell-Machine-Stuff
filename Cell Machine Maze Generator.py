import random
import pyperclip

maze = []

print("How big should the maze be?")
l=int(input())
if l%2==0:
    l+=1
if l<5:
    l=5

_1=[]
for i in range(l):
    _1.append(3)
_2=[]
_2.append(3)
for i in range(l-2):
    _2.append(1)
_2.append(3)

maze.append(_1)
for i in range(l-2):
    maze.append(_2[:])
maze.append(_1)

maze[1][1] = 0

mazex,mazey = (1,1)

randomwaybegin = random.randint(1,2)
if randomwaybegin == 1:
    maze[mazey][mazex] = 0
    maze[mazey][mazex+1] = 0
    maze[mazey][mazex+2] = 0
    mazex = mazex+2
else:
    maze[mazey][mazex] = 0
    maze[mazey+1][mazex] = 0
    maze[mazey+2][mazex] = 0
    mazey = mazey+2

while (mazex!=1)or(mazey!=1):
    
    ways = []
    if maze[mazey][mazex+1]==1:
        if maze[mazey][mazex+2]==1:
            ways.append("r")
    if maze[mazey][mazex-1]==1:
        if maze[mazey][mazex-2]==1:
            ways.append("l")
    if maze[mazey+1][mazex]==1:
        if maze[mazey+2][mazex]==1:
            ways.append("d")
    if maze[mazey-1][mazex]==1:
        if maze[mazey-2][mazex]==1:
            ways.append("u")
    if ways!=[]:
        randomnum = random.randint(0,len(ways)-1)
        waytogo = ways[randomnum]
        
        if waytogo == "r":
            maze[mazey][mazex] = 0
            maze[mazey][mazex+1] = 0
            maze[mazey][mazex+2] = 0
            mazex = mazex+2
        elif waytogo == "l":
            maze[mazey][mazex] = 0
            maze[mazey][mazex-1] = 0
            maze[mazey][mazex-2] = 0
            mazex = mazex-2
        elif waytogo == "d":
            maze[mazey][mazex] = 0
            maze[mazey+1][mazex] = 0
            maze[mazey+2][mazex] = 0
            mazey = mazey+2
        elif waytogo == "u":
            maze[mazey][mazex] = 0
            maze[mazey-1][mazex] = 0
            maze[mazey-2][mazex] = 0
            mazey = mazey-2
    else:
        while ways == []:
            
            if (mazex==1)and(mazey==1):
                break
            
            if maze[mazey][mazex+1]==0:
                maze[mazey][mazex] = 4
                maze[mazey][mazex+1] = 4
                mazex+=2
            elif maze[mazey][mazex-1]==0:
                maze[mazey][mazex] = 4
                maze[mazey][mazex-1] = 4
                mazex-=2
            elif maze[mazey+1][mazex]==0:
                maze[mazey][mazex] = 4
                maze[mazey+1][mazex] = 4
                mazey+=2
            elif maze[mazey-1][mazex]==0:
                maze[mazey][mazex] = 4
                maze[mazey-1][mazex] = 4
                mazey-=2

            if maze[mazey][mazex+1]==1:
                if maze[mazey][mazex+2]==1:
                    
                    ways.append("r")
            if maze[mazey][mazex-1]==1:
                if maze[mazey][mazex-2]==1:
                    
                    ways.append("l")
            if maze[mazey+1][mazex]==1:
                if maze[mazey+2][mazex]==1:
                    
                    ways.append("d")
            if maze[mazey-1][mazex]==1:
                if maze[mazey-2][mazex]==1:
                    
                    ways.append("u")
        if ways!=[]:
            randomnum = random.randint(0,len(ways)-1)
            waytogo = ways[randomnum]
            
            if waytogo == "r":
                maze[mazey][mazex] = 0
                maze[mazey][mazex+1] = 0
                maze[mazey][mazex+2] = 0
                mazex = mazex+2
            elif waytogo == "l":
                maze[mazey][mazex] = 0
                maze[mazey][mazex-1] = 0
                maze[mazey][mazex-2] = 0
                mazex = mazex-2
            elif waytogo == "d":
                maze[mazey][mazex] = 0
                maze[mazey+1][mazex] = 0
                maze[mazey+2][mazex] = 0
                mazey = mazey+2
            elif waytogo == "u":
                maze[mazey][mazex] = 0
                maze[mazey-1][mazex] = 0
                maze[mazey-2][mazex] = 0
                mazey = mazey-2
        else:
            break

maze[l-2][l-2] = 2

code = "V1;"+str(l)+";"+str(l)+";;"

for i in range(len(maze)):
    for j in range(len(maze[i])):
        if (maze[i][j] == 1)or(maze[i][j] == 3):
            code = code + "6.0." + str(j) + "." + str(l - 1 - i) + ","

pyperclip.copy(code)
