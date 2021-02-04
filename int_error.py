import numpy as np

n1 = np.int16()
n2 = np.int32()

def findNmax(n):
    while (n+1)/(n+1) == 1:
        n=+1
    return n

N = findNmax(n1)

print(N)