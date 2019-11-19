from functools import reduce

def calc(n, s):
    l = [4, 2, -43, 5, 6, 0]

    if n == len(l)-1:
        return s
    else:
        temp = calc(n + 1, s+l[n+1])
        return temp

print(calc(-1, 0))



######################

def calc2():
	l = [4, 2, -43, 5, 6, 0]
	sum_all = reduce(lambda x,y: x + y, l)
	return sum_all

print(calc2())



