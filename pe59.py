import time
start=time.time()

def secretcode(stlist,a,b,c):
    s=''
    i=0
    while i!=len(stlist):
        s+=chr(int(stlist[i])^ord(a))+chr(int(stlist[i+1])^ord(b))+chr(int(stlist[i+2])^ord(c))
        i=i+3
    return s

def asciisum(string):
    s=0
    for i in string:
        s+=ord(i)
    return s
        
a=open("cipher.txt",'r')
slist=a.read().split(",")
slist=slist[0:-1]+[0]*(3-(len(slist)-1)%3)

lttrs=list("abcdefghijklmnopqrstuvwxyz")
def answer():
    for i in lttrs:
        for j in lttrs:
            for k in lttrs:
                if " the " in secretcode(slist,i,j,k):
                    return asciisum(secretcode(slist,i,j,k)[0:-2])
print answer()

end=time.time()-start
print "Elapsed time is %f seconds"%end

