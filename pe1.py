import time
p=time.time()

s=0
i=0
while i < 1000:
    if i % 3 == 0 or i % 5 == 0:
        s+=i
    i=i+1
print(s)

e=time.time()-p
print e
