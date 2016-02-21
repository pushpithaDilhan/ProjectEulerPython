import time
s=time.time()

def fac(n):
    if n==0:return 1
    else:return n*fac(n-1)

def facsum(a):
    s=str(a)
    r,i=0,0
    while i<len(s):
        r=r+fac(int(s[i]))
        i=i+1
    return r
print sum(facsum(i) for i in range(3,fac(9)) if facsum(i)==i)
e=time.time()-s
print "Elapsed time is %f seconds"%e
