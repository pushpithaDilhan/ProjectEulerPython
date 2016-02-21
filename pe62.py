import time

s=time.time()

def digitlist(i):
    b=list(str(i))
    b.sort()
    return b

def is5nums(n,lis):
    a=list(str(n))
    a.sort()
    r=0
    for i in lis:
        if digitlist(i)==a:
            r=r+1
    if r==5:return True
    else:return False
    
e=[i**3 for i in range(10000)]
d=[]
for i in e:
    if is5nums(i,e):
        d.append(i)
print min(d)

j=time.time()-s
print "elapsed time is %f seconds"%j
