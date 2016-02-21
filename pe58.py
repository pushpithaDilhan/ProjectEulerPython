import time
s=time.time()

def isprime(n):
    for i in range(3,int(n**0.5)+1):
        if n%i==0:return False
    return True

a=range(2,200000,2)*4
a.sort()
d=[]
i=1
for j in a:
    i=i+j
    d.append(i)

pc,dc=0,1
for i in d:
    dc+=1
    if isprime(i):
        pc+=1
    if float(pc)/dc<0.1:
        print range(3,200000,2)[((dc-1)/4)-1]
        break

    
e=time.time()-s
print "Elapsed time is %f seconds"%e
    
