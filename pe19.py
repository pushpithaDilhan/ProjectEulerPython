import time
s=time.time()

a=range(1,31)
b=range(1,32)
nyear=b+range(1,29)+b+a+b+a+b+b+a+b+a+b
leapyear=b+range(1,30)+b+a+b+a+b+b+a+b+a+b
cal=[]
y=range(1901,2001)
for i in y:
    if i%4==0 or i%400==0:
        cal+=leapyear
    else:
        cal+=nyear
cal=cal[5::]
sundays=[]
c=-1
for i in cal:
    c+=1
    if c%7==0:
        sundays.append(i)
        
print sundays.count(1)

e=time.time()-s
print "Elapsed time is %f seconds"%e


