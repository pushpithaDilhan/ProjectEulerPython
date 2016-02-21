from decimal import getcontext,Decimal
import time

p=time.time()
def countsum(strng):
    c=[int(i) for i in strng]
    return sum(c)

a=range(2,100)
for i in range(2,10):
    a.remove(i*i)
    
getcontext().prec=102
b=[]
for i in a:
    s=str(Decimal(i).sqrt()*10**99)[0:100]
    b.append(countsum(s))
print sum(b)

e=time.time()-p
print "Elapsed time is %f seconds"%e
