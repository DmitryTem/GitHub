import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

			 


def triang_num(num = 1):
    while True:
        num += 1
        yield int(num*(num+1)/2)
        
start = timefunc()
print('-'*30)
found_num = triang_num()
divisors = int()
desired = 500




while divisors < desired:
    divisors = 0
    num = next(found_num)
    
    if not num % 2 == 0:
        continue
      
    for i in range(1, int(1 + math.sqrt(num))):
        if num % i == 0:
            divisors += 2
print('Number of divisors: %i \n' %divisors)
print (num)
elapsed = timefunc() - start
print(elapsed)
print('-'*30)

"""
def prime(x):
  n=x
  lst=[2]
  for i in range(3,n):
    for j in lst:
      if j>math.ceil(math.sqrt(i)+1):
          return None
      if i%j==0:
          return x
  else:
      return None
  return 0  """
	
	
"""def trial(x):
  start = timefunc()
  k = 1 
  temp=0
  M=[1]
  while True:
    n = sum(M)
   # if prime(n) is not None:
    L = [i for i in range(1,int(n//2)+1) if n%i==0]
    if len(L)+1>temp:
      temp = len(L)+1
      print(len(L)+1, n)
      elapsed = timefunc() - start
      print(elapsed)
    if len(L)+1 > x:
      return L, n     
    k += 1
    M.append(k)

        

def trial(x):
    start = timefunc()
    temp=0
    divider = div = n = 0
    while divider < 500:
        div += 1
        n += div
   # if prime(n) is not None:
        L = [i for i in range(1,int(n//2)+1) if n%i==0]
        divider = len(L)+1
        if divider>temp:
            temp = divider
            print(divider, n)
            elapsed = timefunc() - start
            print(elapsed)
    return L, n  """   
			 
#start = timefunc()
#print('-'*30)
#print('List:',trial(500))
#print('-'*30)
#elapsed = timefunc() - start
#print(elapsed)