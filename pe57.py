import time
s=time.time()

def isnumden(loopcount):
    q=1;p=2
    temp=p
    p=2*p+1
    q=temp
    for i in range(loopcount-1):
        temp=p
        p=2*p+q
        q=temp
    if len(str(p+q))>len(str(p)):
        return True
    else:return False

count=0
for i in range(3,1000):
    if isnumden(i):
        count+=1
print count

e=time.time()-s
print "Elapsed time is %f seconds"%e
