import time
s=time.time()

def isdiv(i):
    a=[]
    b=range(1,21)
    j=0
    while len(a)!=20:
        if i%b[j]==0:
            a.append(1)
        else:
            return False
            break
        j=j+1
    if len(a)==20:return True

i=2520*11*13*17*19 #answer should be above 2520 & prime numbers should multiply
while True:
    if isdiv(i):
        print i
        break
    i=i+10    #answer should be devided by 10,20 so step size should be 10

e=time.time()-s
print "elapsed time is %f seconds"%e
