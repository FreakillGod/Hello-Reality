from vpython import *
import numpy as np

piston1=cylinder(radius=1, length=3, color=color.blue, opacity=.5)

while True:
    for myLength in np.linspace(1,6,100):
        rate(100)
        piston1.length=myLength
    for myLength in np.linspace(6,1,100):
        rate(100)
        piston1.length=myLength
    for myRadius in np.linspace(1,6,100):
        rate(100)
        piston1.radius=myRadius
    for myRadius in np.linspace(6,1,100):
        rate(100)
        piston1.radius=myRadius
    for myOpacity in np.linspace(1,0,100):
        rate(100)
        piston1.opacity=myOpacity
    for myOpacity in np.linspace(0,1,100):
        rate(100)
        piston1.opacity=myOpacity