import math
import pyperclip

ogcode = pyperclip.paste()

code = ogcode.split(",")
code[0] = code[0].split(";")
levelsizex = int(code[0].pop(1))
levelsizey = int(code[0].pop(1))
code[0].remove("V1")
code[0] = code[0][1]
code[len(code)-1] = code[len(code)-1].replace(";","")

ogcode = ogcode[:-2]

for i in range(len(code)):
    code[i] = code[i].split(".")

intcode = []

for cell in code:
    intcell = [int(i) for i in cell]
    intcode.append(intcell)

code = intcode

corners = []

for i in range(len(code)):
    if code[i][0]==8:
        corners.append(code[i])
        
for corner in corners:
    corner.pop(0)
    corner.pop(0)

x = [corners[0][0],corners[1][0],corners[2][0],corners[3][0]]
y = [corners[0][1],corners[1][1],corners[2][1],corners[3][1]]
minx = min(x)
maxx = max(x)
miny = min(y)
maxy = max(y)

vaultx,vaulty = (maxx-minx-1,maxy-miny-1)

for i in range(vaultx+1):
    for j in range(vaulty+2):
        ogcode = ogcode+",5.0."+str(minx+i)+"."+str(maxy+j)

for i in range(vaultx+1):
    for j in range(vaulty+2):
        ogcode = ogcode+",0.1."+str(minx+i)+"."+str(vaulty+2+maxy+j)

for i in range(vaultx+1):
    ogcode = ogcode+",8.0."+str(minx+i)+"."+str(miny)

for i in range(vaulty*3+4):
    ogcode = ogcode+",4.1."+str(minx-2)+"."+str(miny+1+i)
    ogcode = ogcode+",4.1."+str(maxx+1)+"."+str(miny+1+i)
    ogcode = ogcode+",5.0."+str(minx-1)+"."+str(miny+1+i)
    ogcode = ogcode+",5.0."+str(maxx)+"."+str(miny+1+i)

for i in range(len(code)):
    if code[i][0] == 4:
        if (code[i][1] == 0)or(code[i][1] == 2):
            ogcode = ogcode+",1.0."+str(code[i][2]-1)+"."+str(code[i][3]+vaulty+1)

    elif (code[i][0] == 3)or(code[i][0] == 0):
        if (code[i][1] == 1):
            ogcode = ogcode+",2.0."+str(code[i][2]-1)+"."+str(code[i][3]+vaulty+1)
        elif (code[i][1] == 3):
            ogcode = ogcode+",1.0."+str(code[i][2]-1)+"."+str(code[i][3]+vaulty+1)

pyperclip.copy(ogcode)
