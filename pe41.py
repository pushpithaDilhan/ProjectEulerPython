import string,time
from itertools import permutations

s=time.time()

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
c=[]
a=list('1234567')
for i in permutations(a):
    b=string.join(i).replace(" ",'')
    if isprime(int(b)):
        c.append(int(b))
print max(c)

e=time.time()-s
print "Elapsed time is %f seconds"%e
