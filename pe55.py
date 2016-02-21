import time
s=time.time()

def ispalin(n):
    if str(n)==str(n)[::-1]:
        return True
    else:return False

def iter_count(i):
    c=0
    while True:
        j=int(int(str(i))+int(str(i)[::-1]))
        c=c+1
        i=j
        if ispalin(j) or c>50:
            return c
print len([i for i in range(10000) if iter_count(i)==51])

e=time.time()-s
print "Elapsed time is %f seconds"%e
