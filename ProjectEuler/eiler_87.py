import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше
			 
""" Наименьшее число, которое можно представить в виде суммы квадрата простого числа, куба простого числа и четвертой степени простого числа,
 равно 28. Между прочим, существует ровно 4 таких числа меньше пятидесяти, которые можно представить в виде суммы указанным способом:

28 = 22 + 23 + 24
33 = 32 + 23 + 24
49 = 52 + 23 + 24
47 = 22 + 33 + 24

Сколько чисел до пятидесяти миллионов можно представить в виде суммы квадрата, куба и четвертой степени простых чисел? """			 
			 
			 
			 
			 
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
    
    
    
def pow_sum(maximum):
    number = 0
    n1 = int(math.sqrt(maximum))+1
    n2 = int(maximum**(1/3))+1
    n3 = int(maximum**(1/4))+1
    M = set()
    L1 = eratosfen(n1)
    L2 = L1[:]
    L3 = L1[:]
    print(L1)
    for i in L1:
        iv = i**2
        for j in L2:
            jv = j**3
            for k in L3:
                summa = iv + jv + k**4
                if summa <= maximum:
                    M.add(summa)
                    #print(i,j,k,summa)
     
    print (M)
    return len(M)





start = timefunc()
print('Number ===',pow_sum(50))
elapsed = timefunc() - start
print(elapsed)       
print('-'*100)






  