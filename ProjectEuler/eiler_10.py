import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше
			 
			 
			 



#Simple element 
def simple(x):
    temp = math.ceil(math.sqrt(x)+1)
    L = [i for i in range(2,temp) if x%i==0 and i!= x]
    if not L:
        return x
    return None 


#Eratosfen
def prime(x):
    a = list(range(x+1))
    a[1] = 0
    lst = []
    i=2
    while i <= x:
        if a[i] !=0:
            lst.append(a[i])
            for j in range(i,x+1,i):
                a[j] = 0
        i += 1
    return lst 
    


start = timefunc()
print('Prime===',sum(prime(2000000)))
elapsed = timefunc() - start
print(elapsed)       
print('-'*100)



#---------------------------------------------------------------
start = timefunc()
n=2000000
temp = math.ceil(math.sqrt(n)+1)
lst=[2]
for i in range(3,n):
    for j in lst:
        if j>math.ceil(math.sqrt(i)+1):
            lst.append(i)
            break
        if i%j==0:
            break
    else:
        lst.append(i)
print('Main===',sum(lst))
elapsed = timefunc() - start
print(elapsed)



#start = timefunc()
#print('Sum===',find_sum(100000))
#elapsed = timefunc() - start
#print(elapsed)
#print('-'*100)

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



  