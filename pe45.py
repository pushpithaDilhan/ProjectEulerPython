import time
s=time.time()

a=[i*(i+1)/2 for i in range(286,100000)]
b={i*(3*i-1)/2:i for i in range(165,100000)}
c={i*(2*i-1):i for i in range(143,100000)}
for i in a:
    if b.has_key(i) and c.has_key(i):
        print i
        break
e=time.time()-s
print "Elapsed time is %f seconds"%e


