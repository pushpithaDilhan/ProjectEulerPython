import time
s=time.time()

def digitsum(x):
    a=list(str(x))
    b=[]
    for i in a:
        b.append(int(i))
    return sum(b)
c=[]
for a in range(1,100):
    for b in range(1,100):
        x=a**b
        c.append(digitsum(x))
print max(c)

e=time.time()-s
print "elapsed time is %f seconds"%e
