import time, sys, math
if sys.platform[:3] == 'win':
    timefunc = time.clock
else:
    timefunc = time.time

#start = timefunc()
#elapsed = timefunc() - start
#


# def find_seq(x):
#     while True:
#         temp_mul = 1
#         temp_sum = 0
#         prime_num = 0
#         L=[1 for i in range(0,x)]
#         for j in range(0,x):
#             temp_mul=temp_mul*L[j]
#             temp_sum=temp_sum+L[j]
#         if temp_mul==temp_sum:
#             return sum(L)
#     return None

def create_matrix(x):
    L = [[0 for j in range(x)] for i in range(x**x)]
    i=0
    k=x
    M = [i+1 for i in range(x)]
    for i in range(x**x):
        for j in range(x):
            a=0
            ##Все неверно
    return


    for i in range(0,x**x):
        print(L[i][1],L[i][1],L[i][2])
    return L


def main(k):
    L=[]
    for i in range(2,k):
        #L.append(k)
        print('-'*100)
        create_matrix(2)
    return None



start = timefunc()
create_matrix(3)
elapsed = timefunc() - start