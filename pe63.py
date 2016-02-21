import time

s=time.time()

r=0
for i in range(1,100):
    for k in range(1,22):
        a=i**k
        if len(str(a))==k:
            r=r+1
print r

e=time.time()-s
print "elapsed time is %f seconds"%e
