import time, sys, math, collections # В Windows использовать time.clock
import numpy as np
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
             # лучшее разреше

start = timefunc()
print('-'*30)

numb= 10000000000
res={}



for i in range(10,numb+1):
    sqr = len(str(i))
    x = round(i**(1./sqr),3)
    if x**sqr==i:
        f = open('e_63.txt', 'a')
        f.write('Num: ' + str(i) + ' Stepen: '+ str(sqr) + '\n')
        print(('Num: ' + str(i) + ' Stepen: '+ str(sqr) + '\n'))
        res[i] = sqr
        f.close()






print('Result: ', res)
print(len(res))
print('-'*30)
elapsed = timefunc() - start
print(elapsed)
