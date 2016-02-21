import time
q=time.time()

def isperm(a,b,c):
    d=list(str(a));d.sort()
    e=list(str(b));e.sort()
    f=list(str(c));f.sort()
    if d==e==f:return True
    else:return False

def isprime(n):
    if n%2==0 or n%3==0:
        return False
    f=6
    while n**0.5>f:
        if n%(f-1)==0 or n%(f+1)==0:
            return False
        f+=6
    return True

prime_list=[i for i in range(1000,10000) if isprime(i)]
a=[]
for i in prime_list:
    for j in range(1000,10000):
        if isprime(i+j) and isprime(i+2*j):
            if isperm(i,i+j,i+2*j):
                a.append(i);a.append(i+j);a.append(i+2*j)
b=a[3::];b.sort()
s=''
for i in b:
    s=s+str(i)
print s

e=time.time()-q
print "Elapsed time is %f seconds"%e
                
                
                
