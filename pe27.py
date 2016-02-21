def isprime(n):
    for i in range(3,int(n**0.5)+1,2):
        if n%i==0:
            return False
    else:return True
def conprimes(a,b):
    c,n=0,0
    while True:
        d=n*n+a*n+b
        if isprime(c):
            c=c+1
        else:break
        n=n+1
    return c
d={}
for a in range(1,10):
    for b in range(1,10):
        d[conprimes(a,b)]=a*b
print d[max(d.keys())]
