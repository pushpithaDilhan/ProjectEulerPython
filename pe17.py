import time
s=time.time()

a=['one','two','three','four','five','six','seven','eight','nine','ten','eleven',
   'twelve','thirteen','fourteen','fifteen','sixteen','seventeen','eighteen',
   'nineteen']
b=['twenty','thirty','forty','fifty','sixty','seventy','eighty','ninety']
c=[]
for i in b:
    for j in a[0:9]:
        x=i+j
        c.append(x)
c=c+a+b
d=[]
for k in a[0:9]:
    for m in c:
        y=k+'hundred'+'and'+m
        d.append(y)
d=d+c

for k in a[0:9]:
    y=k+'hundred'
    d.append(y)
d.append('onethousand')

n,e=0,0
while n<len(d):
    e=e+len(d[n])
    n=n+1
print e

q=time.time()-s
print "elapsed time is %f seconds"%q
