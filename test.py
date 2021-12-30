from vpython import *
from time import *

mRadius=3
wallHeight=30
wallWidt=60



floor1=box(pos=vector(0,-1*wallHeight,0),color=color.cyan,size=vector(wallHeight*2,0.2,wallHeight*2))
floor2=box(pos=vector(0,wallHeight,0),color=color.red,size=vector(wallHeight*2,0.2,wallHeight*2))

wallLeft=box(pos=vector(-1*wallHeight,0,0),color=color.purple,size=vector(0.2,wallHeight*2,wallHeight*2))
wallRight=box(pos=vector(wallHeight,0,0),color=color.purple,size=vector(0.2,wallHeight*2,wallHeight*2))
backwall=box(pos=vector(0,0,-1*wallHeight),color=color.red,size=vector(wallHeight*2,wallHeight*2,0.2))

ball=sphere(pos=vector(0,-20,-10),color=color.yellow,radius=mRadius)
ball1=sphere(pos=vector(0,0,0),color=color.blue,radius=5)


deltaX=.1
xPos=0

bXpos=0
bDeltaX=.05



while True:
    rate(1000)
    xPos+=deltaX
    if (xPos>26 or xPos<-26):
        deltaX*=-1
        
    ball.pos=vector(xPos,0,0)


    bXpos+=bDeltaX
    if (bXpos>25 or bXpos<-25):
        bDeltaX=bDeltaX*-1
    bDeltaX
    ball1.pos=vector(bXpos,bXpos,bXpos)
    
while True:
    pass    
