import time
s=time.time()

def ispan(n):
    s=''
    for i in range(1,9):
        s=s+str(n*i)
        a=list(s)
        a.sort()
        if a==list('123456789') and len(a)==9:
            return s
    else:return '0'
    
a=[]
for i in range(1,9876):
    if len(ispan(i))>0:
        a.append(int(ispan(i)))
print max(a)

e=time.time()-s
print "Elapsed time is %f seconds"%e
