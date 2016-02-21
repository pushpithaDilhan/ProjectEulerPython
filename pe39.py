import time
s=time.time()

d={}
def numsol(i):
    r=0
    for a in range(i/2):
        for b in range(i/2):
            c=a+b+(a*a+b*b)**0.5
            if i==c and a*b!=0:
               r=r+1
    return r
for i in range(1,1001):
    d[numsol(i)]=i
e=d.keys()
print d[max(e)]

e=time.time()-s
print "Elapsed time is %f seconds"%e

    

