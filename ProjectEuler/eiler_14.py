import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

			 


def rule(x):
    i=1
    while x > 1:
        if x % 2 == 0:
            x=x//2
        else:
            x=3*x + 1
        i+=1
    return i

    
start = timefunc()
print('-'*30)
temp = 0
for i in range(2,1000001):
    f=rule(i)
    if temp<f:
        temp = f
        first_element = i
print('Element:',first_element)
print('-'*30)
elapsed = timefunc() - start
print(elapsed)

#---------------------------------
#--------not my recursive---------
#---------------------------------
print('-'*30+'NOT MY'+'-'*30)

C = {1:1}
def chainlength(x):
    if x not in C:
        C[x] = chainlength(x//2 if x%2==0 else 3*x+1)+1
    return C[x]
    
start = timefunc()
print('-'*30)

best = 1
for i in range(2,1000001):
    if chainlength(i) > chainlength(best):
        best = i
    
print('Element:',best, C)
print('-'*30)
elapsed = timefunc() - start
print(elapsed)