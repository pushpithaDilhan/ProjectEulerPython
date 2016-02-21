import time
p=time.time()

d={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
   'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
def sumname(s):
    c,i=0,0
    while i<len(s):
        c=c+d[s[i]]
        i=i+1
    return c
a =open('pe42.txt').read().replace('"', '').split(',')
b=[]
i=0
while i<len(a):
    c=sumname(a[i])
    b.append(c)
    i=i+1
    
q=[]
i=1
while i<200:
    x=i*(i+1)/2
    q.append(x)
    i=i+1

r=0
for i in b:
    if q.count(i)>0:
        r=r+1
print r
        
e=time.time()-p
print "Elapsed time is %f seconds"%e
    

    
