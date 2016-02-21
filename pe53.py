import time
from math import factorial

s=time.time()

b=[]
for n in range(1,101):
    for r in range(0,n):
        a=factorial(n)/(factorial(r)*factorial(n-r))
        if a>1000000:
            b.append(a)
print len(b)

e=time.time()-s
print "elapsed time is %f seconds"%e
