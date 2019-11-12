import time, sys # В Windows использовать time.clock
import math, datetime, time
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

def number_sum():
    L = []
    R = []
    for i in range(12,28124):
        s = 0
        for j in range (1,i):
            if i%j==0:
                s += j
        if s > i:
            L.append(i)
            print(i)
    print('-'*40)
    for i in L:
        for j in L:
            s = i + j
            if s < 21824:
                R.append(s)
                print(s)
    s = 0
    print('-'*40)
    
    mnoj = {i for i in range(0,21824)}
    R = set(R)
    dif = set.difference(mnoj,R)
  

    return s
    
		 
			 
start = timefunc()


print('Count: ', number_sum())
elapsed = timefunc() - start
print(elapsed)



