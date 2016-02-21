import time
s=time.time()

d={}
for i in range(1,1000000):
    b=float(3*i-1)/7
    d[b]=float(b)/i

max=0
num=0
for i in range(1,1000000):
    if d.has_key(float(i)):
        if d[float(i)]>max:
            max=d[float(i)]
            num=i
print num

e=time.time()-s
print "Elapsed time is %f seconds"%e
