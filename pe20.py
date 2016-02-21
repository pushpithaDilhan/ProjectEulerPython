import time
s=time.time()

def fac(n):
    if n==1:
        return 1
    else:
        return n*fac(n-1)
a=list(str(fac(100)))
b,j=0,0
while j<len(a):
    b=b+int(a[j])
    j=j+1
print b

e=time.time()-s
print "elapsed time is %f seconds"%e
    
