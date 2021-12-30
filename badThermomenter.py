from vpython import *
import numpy as np

body=box(pos=vector(0,0,0), color=color.cyan, size=vector(6,20,2))
bar=box(pos=vector(0,0,1), color=color.red, length=1, width=1, height=18)    #size=vector(1,18,1)
ball=sphere(pos=vector(0,-9.5,1), radius=1, color=color.red)


while True:
    for mybar in np.linspace(5,18,500):
        rate(200)
        bar.height=mybar
    # for movement in np.linspace(0,-9.5,500):
    #     rate(200)
    #     bar.pos=movement



while True:
    pass    
