import time
s=time.time()

c=[]
for a in range(2,101):
    for b in range(2,101):
        c.append(a**b)
        c.append(b**a)
print len(set(c))

e=time.time()-s
print "elapsed time is %f seconds"%e
