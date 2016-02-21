n=2
for i in range(7830456):
    n=(2*n)%10000000000
print str(n*28433+1)[len(str(n*28433+1))-10:]
    
