import time
s=time.time()

a=0
for i in range(1,1001):
    a=a+i**i
print str(a)[-10:]

e=time.time()-s
print "elapsed time is %f seconds"%e
