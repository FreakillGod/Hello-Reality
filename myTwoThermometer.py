from vpython import *
import numpy as np


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
while True:
    for Temp in np.linspace(1,4.4,500):
        rate(200)
        mercuryBar1.length=Temp
    for Cold in np.linspace(4.5,1,500):
        rate(200)
        mercuryBar2.length=Cold



while True:
    pass



