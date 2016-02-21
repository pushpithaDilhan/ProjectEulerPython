import time
s=time.time()

import math
def solve():
    for i in range(1,1000):
        for j in range(1,1000):
            if i+j+math.sqrt(i*i+j*j)==1000:
                print i*j*math.sqrt(i*i+j*j)
                return

solve()
e=time.time()-s
print "elapsed time ",e,"seconds"
            
