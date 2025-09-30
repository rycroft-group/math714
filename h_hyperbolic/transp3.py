#!/usr/bin/python3
import numpy as np
from math import exp

# Grid size
m=256
u=np.empty((m))
v=np.empty((m))
w=np.empty((m))
snaps=100
iters=10
z=np.empty((m,snaps+1))

# PDE-related constants
c=0.1
dx=1.0/m
dt=0.01
nu=c*dt/dx

# Initial condition
def f(x):
    #    return exp(-20*(x-0.5)**2)
    if x<0.25 or x>0.75:
        return 0
    else:
        return 1

# Set up initial condition at timestep 0 and timestep -1
for i in range(m):
    x=dx*i
    u[i]=f(x)
    w[i]=f(x-dt)
z[:,0]=u

# Integrate the PDE using the leapfrog method
for i in range(1,snaps+1):
    for k in range(iters):
        v[:]=w-nu*(np.roll(u,-1)-np.roll(u,1))

        # Cycle pointers to the three arrays
        y=w;w=u;u=v;v=y
    z[:,i]=u

# Output results
for j in range(m):
    e=[str(j*dx)]
    for i in range(snaps+1):
        e.append(str(z[j,i]))
    print(" ".join(e))
