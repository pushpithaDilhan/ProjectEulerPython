import time
from itertools import permutations

s=time.time()
def listnum(list):
    s=''
    for i in list:
        s=s+str(i)
    return int(s)
b=[0,2,3,5,7,11,13,17]
def isprop(n):
    a=str(n)
    if int(a[1:4])%2==0 and int(a[2:5])%3==0 and int(a[3:6])%5==0 and int(a[4:7])%7==0 and int(a[5:8])%11==0 and int(a[6:9])%13==0 and int(a[7:10])%17==0:return True
    else:return False
    return True
c=[]
d=[1,2,3,4,5,6,7,8,9,0]
for i in permutations(d):
    if i[0]!=0 and isprop(listnum(i)):
        c.append(listnum(i))
print sum(c)
e=time.time()-s
print "Elapsed time is %f seconds"%e


