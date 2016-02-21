import time
s=time.time()

def isprime(n):
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    else:return True

a=17
i=9
while i<2000000:
    if isprime(i):
        a=a+i
    i=i+2
print a

e=time.time()-s
print "elapsed time is %f Seconds"%e
