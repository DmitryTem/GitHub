"""
Простые числа 3, 7, 109 и 673 достаточно замечательны. Если взять любые два из них и объединить их в произвольном порядке,
в результате всегда получится простое число. Например, взяв 7 и 109, получатся простые числа 7109 и 1097.
Сумма этих четырех простых чисел, 792, представляет собой наименьшую сумму элементов множества из четырех простых чисел, 
обладающих данным свойством.

Найдите наименьшую сумму элементов множества из 5 простых чисел, для которых объединение любых двух даст новое простое число.
"""

import time, sys, math, collections 
import numpy as np
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time 
             

             

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

def compare(l):
    for i in range(len(l)):
        for j in range(i,len(l)):
         s1 = str(l[j]) + str(l[i])
         s2 = str(l[i]) + str(l[j])
         if int(s1) not in lst or not int(s2) in lst:
             return None
    return n
            
    

def find_topfive(L):
    temp = []
    for i in len(L):
        k=0
        #print(L)
        s=str(i)
        for j in range(len(s)):
            print(j)
            if int(j) in L:
                k+=1
                temp.append(s[j])
                temp.append(s[j:])
                
                if k > 5:
                    if compare(temp):
                        print(temp)
        del temp[:]
    return None
    

lst = eratosfen(100000)




start = timefunc()
print('-'*30)
print('Result: ', find_topfive(lst))
print('-'*30)
elapsed = timefunc() - start
print(elapsed)
