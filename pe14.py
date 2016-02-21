import time
s=time.time()

a=[]
def coll(x):
    if x==1:
        a.append(1)
    elif x%2==0:
        a.append(x)
        x=x/2
        coll(x)
    else:
        a.append(x)
        x=3*x+1
        coll(x)
b={}
i=1
while i<1000000:
    coll(i)
    b[len(a)]=i
    a=[]
    i=i+1

c=b.keys()
print b[max(c)]

e=time.time()-s
print "elapsed time is %f seconds"%e 

    
