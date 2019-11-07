import time, sys # В Windows использовать time.clock
import math, datetime, time
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

			 
def swap (x,y):
    tmp = x
    x = y
    y = tmp
    print('swap',x,y)
    return x,y
			 
			 
L = []
L.sort()
def next_perem(k, A, size):
    global L
    if (k==size):
        print('--------------------------')
        L.append(int("".join(A)))
        
        
     

    for i in range(k,size):
        print(A,1, 'k='+str(k))
        A[k],A[i] = swap(A[k],A[i])
        print(A,2, 'k='+str(k))
        next_perem(k+1,A,size)
        print(A,3, 'k='+str(k))
        A[k],A[i] = swap(A[k],A[i])
        print(A,4, 'k='+str(k))
    return A
			 
def main():
    n = 3
    A = [str(i) for i in range(n)]
    
    next_perem(0,A,n)
		 
			 
start = timefunc()

#print('Count: %d' %(find_sunday_count()))
main()

L.sort()
#print('Count: ', L[1000000])
#print('Count: ', L[999999])
elapsed = timefunc() - start
print(elapsed)



#start = timefunc()
#print('Sum===',find_sum(100000))
#elapsed = timefunc() - start
#print(elapsed)
#print('-'*100)
