import time

s=time.time()

def issamedigits(n):
    a=list(str(n*2))
    b=list(str(n*3))
    c=list(str(n*4))
    d=list(str(n*5))
    e=list(str(n*6))
    a.sort()
    b.sort()
    c.sort()
    d.sort()
    e.sort()
    if a==b==c==d==e:return True
    else:return False

i=1
while True:
    if issamedigits(i):
        print i
        break
    i=i+1

e=time.time()-s
print "elapsed time is %f seconds"%e
