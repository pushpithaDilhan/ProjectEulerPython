import time
s=time.time()

a=str(2**1000)
b=int(a[0])
i=0
while i<len(a)-1:
    b=b+int(a[i+1])
    i=i+1
print b

e=time.time()-s
print "elapsed time ",e,"seconds"
