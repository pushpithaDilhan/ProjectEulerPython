p={0:1,1:2}
def fibo(n):
    if p.has_key(n):
        return p[n]
    else:
        nw=fibo(n-1)+fibo(n-2)
        p[n]=nw
        return nw
a={}
n=0
while fibo(n)<4000000:
    if fibo(n)%2==0:
        a[n]=fibo(n)
    n=n+1
b=a.values()
print sum(b)

