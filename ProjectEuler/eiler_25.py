import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

			 
def fibonachi():
    flag = True
    l = [1,1]
    i = 2
    while flag:
        f = l[i-1] + l[i-2]
        l.append(f)
        if len(str(f)) == 1000:
            print(f, i)
            flag = False
            break
        i+=1
    return i+1


			 
			 
			 
			 

start = timefunc()
print('-'*30)  
print('Position:',fibonachi())
print('-'*30)
elapsed = timefunc() - start
print(elapsed)