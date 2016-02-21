import time
s=time.time()

def isprime(n):
    for i in range(2,int(n**0.5)+1):
        if n%i==0:
            return False
    return True
a=[2,3,5,7,11,13]
i=17
while sum(a)<1000000:
    if isprime(i):
        a.append(i)
    i=i+2
b=[]
for i in range(len(a)):
    for j in range(i,len(a)):
        if isprime(sum(a[i:j])):
            b.append(sum(a[i:j]))
print max(b)

e=time.time()-s
print "Elapsed time is %f seconds"%e
