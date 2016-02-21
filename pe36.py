import time
s=time.time()

def ispal(n):
    if str(n)==str(n)[::-1]:
        return True
    else:return False

a=[]
for n in range(1,1000000):
    if ispal(n) and ispal(str(bin(n))[2:]):
        a.append(n)
print sum(a)

e=time.time()-s
print "elapsed time is %f seconds"%e
    
