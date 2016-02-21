import time
s=time.time()

def isprime(n):
    if n%2==0 or n%3==0:
        return False
    f=6
    while n**0.5>f:
        if n%(f-1)==0 or n%(f+1)==0:
            return False
        f+=6
    return True

def circularprimes(n):
    s=str(n)
    for i in range(len(s)):
        x=s[1:len(s)]+s[0]
        if isprime(int(x)):
            s=x
        else:return False
    return True

j=13
for i in range(101,1000000,2):
    if isprime(i):
        if circularprimes(i):
            j+=1

print j

e=time.time()-s
print "Elapsed time is %f seconds"%e
