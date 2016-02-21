import time
s=time.time()

from itertools import combinations
def divisorsum(n):
    a=[]
    for i in range(1,n):
        if n%i==0:
            a.append(i)
    return sum(a)

c=range(0,28124)
bb=[i for i in c if divisorsum(i)>i]
f=[2*i for i in bb if 2*i<28124]
a=[sum(i) for i in combinations(bb,2) if sum(i)<28124]+f
b=list(set(a))

n=0
for i in range(28124):
    if i not in b:
        n+=i

print n

e=time.time()-s
print "Elapsed time is %f seconds"%e





