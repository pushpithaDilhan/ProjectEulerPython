import time
s=time.time()

from itertools import permutations
def listnum(list):
    s=''
    for i in list:
        s+=str(i)
    return int(s)

a=range(10)
c=0
for i in permutations(a):
    c+=1
    if c==1000000:
        print listnum(i)
        break

e=time.time()-s
print "Elapsed time is %f seconds"%e
