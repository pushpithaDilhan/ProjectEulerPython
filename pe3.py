import time
start=time.time()
def factor(x):
    n=2
    while True:
        if x==n:
            print n
            break
        elif x/n==0:
            factor(x)
            break
        elif x%n==0:
            print n
            x=x/n
        n=n+1


print factor(600851475143)
elapsed=time.time()-start
print "elapsed time is ",elapsed,"seconds"

#######################################################
#######################################################

import time
start=time.time()
x=600851475143
n=2
while x!=1:
    while x%n==0:
        x=x/n
    n=n+1
print n-1
elapsed=time.time()-start
print "elapsed time is ",elapsed



