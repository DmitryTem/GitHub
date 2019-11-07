import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше
			 
			 
			 
			 
			 



# Простые
"""import math
start = timefunc()
res = []
x=2
start = timefunc()
while len(res) != 10001:
    temp = math.ceil(math.sqrt(x)+1)
    L = [i for i in range(2,temp) if x%i==0 and i!= x]
    #print(L, x)
    if not L:
        res.append(x)
       # print(res)
    x+=1
K = [j for j in range(1,10002)]
Dic = dict(zip(K,res))
print(Dic)
elapsed = timefunc() - start
print(max(res), elapsed)"""


#Simple element 
def simple(x):
    temp = math.ceil(math.sqrt(x)+1)
    L = [i for i in range(2,temp) if x%i==0 and i!= x]
    if not L:
        return x
    return None

#Trial 
def trial(a):
    element = a      
    flag=False
    while flag==False:
        S = list(str(element)) 
        if simple(element):
            E=list(str(element))
            for i in range(0,10):
                #print(S, len(S), i)
                if E.count(str(i)) == 3 and E[0]!='0':
                    #print(S, len(S), i)
                    P = [j for j in range(0, len(S)) if str(i) == S[j]]
                    #print(P, len(P))
                    res = last_trial(element,int(P[0]),int(P[1]),int(P[2]))
                    if res is not None:
                        return res
        element+=1
    return None


def last_trial(a,p1,p2,p3):
    L=list(str(a))
    res=[]
    for i in range(0,10):
        L[p1]=i
        L[p2]=i
        L[p3]=i
        M=''.join([str(i) for i in L])
        print(M)
        if simple(int(M)) and L[0]!=0:
            res.append(M) 
        if len(res) == 8:
            return res
    return None

start = timefunc()
first = trial(56000)
print(first)
elapsed = timefunc() - start
print(elapsed)


  