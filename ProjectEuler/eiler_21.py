import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

			 
def find_friendly_numbers():
    k = 10001
    numbers = {}
    for i in range(1,k):
        l = []
        for j in range(1,i):
            if i%j == 0:
                l.append(j)

        numbers[i] = sum(l)
        
    
    print('-----------find-----------')
    
    s=0
    for i in range(1,k):
       for j in range(1,k):
           if i==numbers[j] and j==numbers[i] and i!=j:
               s+= i
               #print(i,numbers[j],j,numbers[i])
               print('Key: %d, Value: %d - Key: %d, Value: %d' %(i,numbers[j],j,numbers[i])) 
    return s

			 
			 
			 
			 

start = timefunc()
print('-'*30)  
print('Summa:',find_friendly_numbers())
print('-'*30)
elapsed = timefunc() - start
print(elapsed)