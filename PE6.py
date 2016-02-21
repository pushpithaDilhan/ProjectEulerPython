a=range(1,101)
b=sum(a)**2
c=[]
i=1
while i<101:
    n=i**2
    c.append(n)
    i=i+1
print b-sum(c)
