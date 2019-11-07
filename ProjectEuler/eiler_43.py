import time, sys, math, collections # В Windows использовать time.clock
import numpy as np

if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше


			 

def pannum_sum(n):
    pan = []
    pan_num = []
    
    for i in range(0,n+1):
        pan.append(str(i))
    print(pan)
    s = ''.join(pan)
    s_rev = ''.join(reversed(pan))
    
    for j in range(int(s),int(s_rev)+1):
        flag = True
        j_str = str(j)
        for k in j_str:
            if j_str.count(k)>1:
                break
        if flag:
            print(j_str)
            pan_num.append(j_str)

    return '____STOP___'
    


start = timefunc()
print('-'*30)
print('Result: ', pannum_sum(9))
print('-'*30)
elapsed = timefunc() - start
#f=open('e_60.txt','a')
#f.write('Time: ' + str(elapsed))
print(elapsed)
#f.close()
