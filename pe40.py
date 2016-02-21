import time
a=time.time()

s='1'
i=2
while len(s)<1000000:
    s=s+str(i)
    i=i+1

b=int(s[0])*int(s[9])*int(s[99])*int(s[999])*int(s[9999])*int(s[99999])*int(s[999999])
print b

e=time.time()-a
print "elapsed time is %f seconds"%e
    
