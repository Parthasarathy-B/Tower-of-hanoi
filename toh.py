# Use Left, Down, Right arraow keys to move the disks from one rod to another rod. 

from turtle import*
import turtle
from pygame import mixer

mixer.init()
mixer.music.load('jack sparrow.mp3')
mixer.music.play(-1)

bc = 'lime'
rc = 'blue'

bgcolor(bc)
hideturtle()
tracer(0)

def gt(x,y):
    penup()
    goto(x,y)
    pendown()

a = [90,75,60,45,30,15]
b = []
c = []

#rod
def rod():
    pensize(7)
    gt(-350,-50)
    fd(50)
    for i in range(3):
        fd(100)
        lt(90)
        fd(200)
        rt(180)
        fd(200)
        lt(90)
        fd(100)
    fd(50)
    pensize(4)
        
fillcolor(rc)
bh=25

#ring
def rings():
    def ring(x):
        for i in range(len(x)):
            begin_fill()
            fd(x[i])
            lt(90)
            fd(bh)
            lt(90)
            fd(x[i]*2)
            lt(90)
            fd(bh)
            lt(90)
            fd(x[i])
            end_fill()
            penup()
            lt(90)
            fd(bh)
            rt(90)
            pendown()

    gt(-200,-50)
    ring(a)
    gt(0,-50)
    ring(b)
    gt(200,-50)
    ring(c)


bln = 0
sn = turtle.Screen()

cnt = 2
step = 0

def steps():
    global step
    step+=1
    pencolor('red')
    gt(-280,230)
    write('Steps : ',font=('Rockwell Nova',20,'normal'),align='center')
    gt(-220,230)
    write(step,font=('Comic Sans MS',20,'normal'),align='center')
    sn.update()
    

def move():
    pencolor(bc)
    dot(10000)
    pencolor('black')
    print(a)
    print(b)
    print(c)
    rod()
    rings()
    steps()
    
    
    
def highlight(x):
    pencolor('yellow')
    fd(x[-1])
    lt(90)
    fd(bh)
    lt(90)
    fd(x[-1]*2)
    lt(90)
    fd(bh)
    lt(90)
    fd(x[-1])
    
eck = True

def funleft():
    global cnt
    global bln
    global eck
    if (cnt % 2 == 0):
        if (len(a)>0):
            gt(-200,(bh*len(a))-75)
            highlight(a)
            sn.update()
            bln=a[-1]
            a.pop()
            eck=True
        else:
            eck=False
    else:
        if (eck == True):
            a.append(bln)
            move()
    cnt += 1

def fundown():
    global cnt
    global bln
    global eck
    if (cnt % 2 == 0):
        if (len(b)>0):
            gt(0,(bh*len(b))-75)
            highlight(b)
            sn.update()
            bln=b[-1]
            b.pop()
            eck=True
        else:
            eck=False
    else:
        if (eck == True):
            b.append(bln)
            move()
    cnt += 1

def funright():
    global cnt
    global bln
    global eck
    if (cnt % 2 == 0):
        if (len(c)>0):
            gt(200,(25*len(c))-75)
            highlight(c)
            sn.update()
            bln=c[-1]
            c.pop()
            eck=True
        else:
            eck=False
    else:
        if (eck == True):
            c.append(bln)
            move()
    cnt += 1

listen()
onkeypress(funleft,'Left')
onkeypress(fundown,'Down')
onkeypress(funright,'Right')

rod()
rings()
pencolor('red')
gt(-280,230)
write('Steps : ',font=('Rockwell Nova',20,'normal'),align='center')

sn.mainloop()
