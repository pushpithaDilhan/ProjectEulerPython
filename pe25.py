import time
s=time.time()

a={0:1,1:1}
def fibo(n):
    if a.has_key(n):
        return a[n]
    else:
        nw=fibo(n-1)+fibo(n-2)
        a[n]=nw
        return nw
i=1
while True:
    if len(str(fibo(i)))==1000:
        print i+1
        break
    i=i+1

e=time.time()-s
print "elapsed time is %f seconds"%e
