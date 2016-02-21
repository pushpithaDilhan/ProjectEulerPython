import time
s=time.time()

def num_factors(n):
    if n%2==0:
        return numfac(n/2)*numfac(n+1)
    else:
        return numfac(n)*numfac((n+1)/2)
def numfac(n):
    r=0
    for i in range(1,n+1):
        if n%i==0:
            r=r+1
    return r
for i in range(1,1000000):
    if num_factors(i)>500:
        print i*(i+1)/2
        break
e=time.time()-s
print "Elapsed time is %f seconds"%e
