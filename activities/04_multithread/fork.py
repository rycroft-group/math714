#!/usr/bin/python3
import os
import sys

tot = 2001  # Total jobs
P = 8  # Available slots
pid = [None]*(P+1)
t = 1  # Set thread number
queue = P == 1  # Set queue status

# Loop over jobs
for i in range(tot):
    print("Job %d to slot %d" % (i, t))
    j = os.fork()  # Fork a child process

    if j == 0:
        ### Write your code here ###
        os._exit(0)
    pid[t] = j

    # If reach the max number of slots,
    # then wait for one job to finish
    if queue:
        # Find available slots
        npid = os.wait()[0]
        t = 1
        while pid[t] != npid:
            t += 1
            if t > P:
                print("PID return error")
                sys.exit()
    # Otherwise, move onto the next slot
    else:
        t += 1
        queue = t >= P

# Wait for all remaining jobs to finish
if queue:
    for i in range(P-1):
        os.wait()
else:
    for i in range(t-1):
        os.wait()