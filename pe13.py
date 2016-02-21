#copy the digits into a txt file in python27 folder(digit.txt)

import time
s=time.time()

b=[]
a=open("digit.txt","r")
i=0
t=0
while i<100:
    t=t+int(a.readline())
    i=i+1
print str(t)[0:10]

e=time.time()-s
print "elapsed time is ",e,"seconds"
