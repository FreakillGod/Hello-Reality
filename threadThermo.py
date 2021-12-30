from vpython import *
import numpy as np
from time import *
from threading import Thread 

def therm1():
    while True:
        for Temp in np.linspace(.1,4.4,250):
            rate(100)
            mercuryBar1.length=Temp
        for Temp1 in np.linspace(4.4,.1,250):
            rate(100)
            mercuryBar1.length=Temp1

def therm2():
    while True:
        for Cold in np.linspace(.1,4.4,500):
            rate(100)
            mercuryBar2.length=Cold
        for Cold in np.linspace(4.4,.1,500):
            rate(100)
            mercuryBar2.length=Cold

tube1=cylinder(length=4.5, radius=.35, color=color.white, opacity=0.3)
bowl1=sphere(radius=.8, color=color.white, opacity=0.3)
mercury1=sphere(radius=.6, color=color.red)
mercuryBar1=cylinder(radius=.25, length=4.3, color=color.red)



tube2=cylinder(length=4.5,pos=vector(0,1.5,0), radius=.35, color=color.white, opacity=0.3)
bowl2=sphere(radius=.8,pos=vector(0,1.5,0), color=color.white, opacity=0.3)
mercury2=sphere(pos=vector(0,1.5,0), radius=.6, color=color.red)
mercuryBar2=cylinder(radius=.25,pos=vector(0,1.5,0), length=4.3, color=color.red)


for ticks in np.linspace(1,4.5,18):
    box(size=vector(.02,.2,.01), pos=vector(ticks,0,.25))
for ticks in np.linspace(1,4.5,18):
    box(size=vector(.02,.2,.01), pos=vector(ticks,1.5,.25))

therm1Thread=Thread(target=therm1)
therm2Thread=Thread(target=therm2)

therm1Thread.daemon=True 
therm2Thread.daemon=True

therm1Thread.start()
therm2Thread.start()