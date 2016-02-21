import time
s=time.time()

max=10000
a={i*(3*i-1)/2:i for i in range(1,max)}
b=[i*(3*i-1)/2 for i in range(1,max)]
e=[]
for i in range(len(b)):
    for j in range(len(b)):
        if i==j:continue
        c=b[i]+b[j]
        d=abs(b[i]-b[j])
        if a.has_key(c) and a.has_key(d):
            e.append(d)
print min(e)
e=time.time()-s
print "Elapsed time is %f seconds"%e
