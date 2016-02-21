import time
s=time.time()

def isnotprime(x):
    for i in range(2,int(x**0.5)+1):
        if x%i==0:
            return True
    else:return False
a=filter(isnotprime,range(1,10000))
b=[]
def sumfac(n):
    c,i=0,1
    while n!=i:
        if n%i==0:
            c=c+i
        i=i+1
    return c

for i in a:
    c=sumfac(i)
    e=sumfac(c)
    if e==i and i!=c:
        b.append(i)
print sum(set(b))

e=time.time()-s
print "elapsed time is %f seconds"%e
