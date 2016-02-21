import time
start=time.time()
a=[]
for i in range(900,1000):
    for j in range(900,1000):
        n=i*j
        a.append(n)
c=[]
for i in a:
    b=str(i)
    d=b[::-1]
    if int(b)==int(d):
        c.append(i)
print max(c)
elapsed=time.time()-start
print "elapsed time is ",elapsed,"seconds"



