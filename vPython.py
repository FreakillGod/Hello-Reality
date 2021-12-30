from vpython import *
from time import *

mRadius=4

floor=box(pos=vector(0,-35,0),color=color.cyan,size=vector(120,0.2,60))
floor2=box(pos=vector(0,25,0),color=color.red,size=vector(120,0.2,60))

wallLeft=box(pos=vector(-60,-5,0),color=color.purple,size=vector(0.2,60,60))
wallRight=box(pos=vector(60,-5,0),color=color.purple,size=vector(0.2,60,60))
backwall=box(pos=vector(0,-5,-30),color=color.red,size=vector(120,60,0.2))

ball=sphere(pos=vector(0,-30,-10),color=color.yellow,radius=mRadius)

deltaX=.1
xPos=0

while True:
    rate(200)
    xPos+=deltaX
    if (xPos>50 or xPos<-50):
        deltaX*=-1
        
    ball.pos=vector(xPos,-20,0)
    
while True:
    pass