import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

			 

def factorial(n):
    res = 1
    while n>1:
       res = res*n
       n = n-1
    return res
    
    
    
start = timefunc() 
L = []
for i in range(3,1000000):
    number_sum = 0
    for j in str(i):
       number_sum += factorial(int(j))
    if number_sum == i:
        L.append(i)
        
   
print('Element: %d' % (sum(L)))
print('-'*30)
elapsed = timefunc() - start
print(elapsed)