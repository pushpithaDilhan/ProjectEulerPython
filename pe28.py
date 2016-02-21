import time
s=time.time()

a=range(2,1001,2)*4
a.sort()
b=[1]
d=1
for i in a:
    d=d+i
    b.append(d)
print sum(b)

e=time.time()-s
print "elapsed time is %f seconds"%e
