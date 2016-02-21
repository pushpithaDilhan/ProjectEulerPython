import time
s=time.time()

def isprime(n):
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    else:return True

a=[2,3,5]
i=7
while len(a)!=10001:
    if isprime(i):
        a.append(i)
    i=i+2
print max(a)

e=time.time()-s
print "elapsed time is %f Seconds"%e
