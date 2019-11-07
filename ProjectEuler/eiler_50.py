import time, sys, math, collections # В Windows использовать time.clock
import numpy as np

if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

			 
def prime(n):
    if n % 2 == 0:
        return n == 2
    d = 3
    while d*d <= n and n % d !=0:
        d += 2
    return d * d > n
    
    
def eratosfen(n):
    a = list(range(n+1))
    a[1] = 0
    L = []
    i = 2
    while i <=n: 
        if a[i] != 0:
            L.append(a[i])
            for j in range(i, n+1, i):
                a[j] = 0
        i += 1
    L.sort()
    return L


    

def find_long_sum(k):
    
    res = []
    max_num = 0
    for i in range(int(k/2)):
        s = 0
        num = 0
        j=i
        while s <= k:
            num+=1
            j+=1
            if s+j>k: break
            if prime(j): 
                s=s+j
        if max_num < num and prime(s):
            max_num = num
            print(s, num)
    return '____STOP____'
    


#way = eratosfen(999999) #999999
print('**'*20)




start = timefunc()
print('-'*30)
print('Result: ', find_long_sum(1000000))
print('-'*30)
elapsed = timefunc() - start
#f=open('e_60.txt','a')
#f.write('Time: ' + str(elapsed))
print(elapsed)
#f.close()
