import time, sys, math, collections # В Windows использовать time.clock
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
    

    
    
def last_list(B, s):
    flag = True
    for i in B: 
        if i > 2: flag = False
    if 1 in B and flag: return s
    Res = []
    L = []
    for num in B:
       if num > 2:
           mid = int(num/2)
           diff = num-2
           while mid < diff:
             # print(mid, diff)
              part = num - diff
              if prime(diff) and prime(part):
                  if diff != part:
                      L.append(diff)
                      L.append(part)
                  else:
                      L.append(diff)
                  if diff != 1 and part != 1:
                      s += 1
                      Res.append(str(diff) + ' + ' + str(part) )
                      print(Res)
              diff -= 1
              
    return last_list(L,s)
    
    """
def find_first_list(num):
    #if num = 1: return None
    mid = int(num/2)
    diff = num-2
    L = []
    Res = []
    s = 0
    while mid <= diff:
        #print(mid, diff)
        part = num - diff
        if prime(diff) and prime(part) and diff > 1 and part > 1:
            if diff != part:
                L.append(diff)
                L.append(part)
            else:
                L.append(diff)
            Res.append(str(diff) + ' + ' + str(part) )
            s += 1
        diff -= 1
    #print(Res)
    
   # s += last_list(L, s)
    print(s)
    return L
    
def min_number_sum(buf):
    i = 0
    start = 10
    res = []
    while True:
        res = find_first_list(start)
        print(res)
        
           
        
        
        #print (mid)
        break
    return 0


def recursia(n, s):   
    if n == 1: return s
    if prime(n) :
        s +=1
        print(n)
    return recursia(n-1, s)
"""
start = timefunc()
print('Number ===',last_list([10],0))
elapsed = timefunc() - start
print(elapsed)       
print('-'*100)






  