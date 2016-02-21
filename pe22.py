import time
s=time.time()

d={'A':1,'B':2,'C':3,'D':4,'E':5,'F':6,'G':7,'H':8,'I':9,'J':10,'K':11,'L':12,'M':13,
   'N':14,'O':15,'P':16,'Q':17,'R':18,'S':19,'T':20,'U':21,'V':22,'W':23,'X':24,'Y':25,'Z':26}
def sumname(s):
    c,i=0,0
    while i<len(s):
        c=c+d[s[i]]
        i=i+1
    return c
a = open('pe22.txt').read().replace('"', '').split(',')
a.sort()
b=[]
i=0
while i<len(a):
    score=(i+1)*sumname(a[i])
    b.append(score)
    i=i+1
print sum(b)

e=time.time()-s
print "Elapsed time is %f seconds"%e
    

    
