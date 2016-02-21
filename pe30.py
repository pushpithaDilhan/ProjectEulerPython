import time
s=time.time()

def fifthsum(n):
    a=str(n)
    r,i=0,0
    while i<len(a):
        r=r+int(a[i])**5
        i=i+1
    return r
a=[]
for i in range(2,295245):
    if fifthsum(i)==i:
        a.append(i)
print sum(a)

e=time.time()-s
print "Elapsed time is %f seconds"%e
