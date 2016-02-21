__author__ = 'Pushpitha'
import time
s=time.time()

def isprime(n):
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    else:return True

print isprime(15485863)
e=time.time()-s
print "elapsed time is %f Seconds"%e

