import time
p=time.time()

def ispan(s):
    a=list(s)
    a.sort()
    if a==list('123456789') and len(a)==9:
        return True
    else:return False
a=[]
for i in range(1,2000):
    for j in range(i,2000):
        s=str(i)+str(j)+str(i*j)
        if ispan(s):
            a.append(i*j)
print sum(set(a))
e=time.time()-p
print "Elapsed time is %f seconds"%e
