#!/usr/bin/python3
import numpy as np
from math import exp

# Matrices
a=np.array([[998,1998],[-999,-1999]])
i=np.identity(2)

# Initial conditions
ue=np.array([[1],[0]])
ui=np.array([[1],[0]])

# Starting time and timestep (currently chosen within the stability region of
# the explicit method)
t=0
k=0.02

while t<2:

    # Print solutions and exact solution
    ex1=2*exp(-t)-exp(-1000*t)
    ex2=-exp(-t)+exp(-1000*t)
    print(t,ex1,ex2,ue[0,0],ue[1,0],ui[0,0],ui[1,0])

    # Explicit step
    ue=ue+k*np.dot(a,ue)

    # Implicit step
    ui=np.linalg.solve(i-k*a,ui)
    t+=k
