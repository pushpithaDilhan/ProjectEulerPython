import time
s=time.time()

def cycle_length(n):
    i=1
    if n%2==0:return cycle_length(n/2)
    if n%5==0:return cycle_length(n/5)
    while True:
        if (pow(10,i)-1)%n==0:return i+1
        else:i+=1
a=[cycle_length(i) for i in range(1,1000)]
print max(a)

e=time.time()-s
print "Elapsed time is %f seconds"%e

