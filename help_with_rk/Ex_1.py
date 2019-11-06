import numpy as np
from timeit import timeit


def mytimeit(fun, *args):
    n = 10
    t = timeit(lambda: fun(*args), number=n) #уменьшили количество повторений
    return t / n                            #так как в wsum3 получается большое количество итераций с входными параметром num из (test)


def wsum1(x, w):
    n = len(x)
    res = 0
    for i in range(n):  # считаем сумму в цикле
        res = res + w[i] * (x[i] ** 2)
    return res


def wsum2(x, w):
    n = len(x)
    m1 = np.eye(n)
    m2 = x
    m3 = x.reshape(-1,1)

    for i in range(n):
        m1[i][i] = w[i]

    res = np.dot(m1, m2)  # умножаем с помощью готовой функции numpy
    res = np.dot(res, m3)
    return float(res)


def wsum3(x, w):
    n = len(x)
    m1 = np.eye(n)
    m2 = x
    m3 = x.reshape(-1,1)
    s = 0
    temp = np.zeros(n)
    for i in range(n):
        m1[i][i] = w[i]
    for i in range(n):
        for j in range(n):
            s = s + m1[i][j] * m3[j]      
        temp[i] = s
        s=0
    for i in range(n):
        s = s + temp[i]*m2[i]    

    return float(s)

def test(x = np.linspace(1, 11, num=1000),w = np.linspace(1, 14, num=1000)):
    print('wsum1:',wsum1(x,w))
    print('wsum2:',wsum2(x,w))
    print('wsum3:',wsum3(x,w))
    print('wsum1 time:',mytimeit(wsum1,x,w))
    print('wsum2 time:',mytimeit(wsum2,x,w))
    print('wsum3 time:',mytimeit(wsum3,x,w))

















