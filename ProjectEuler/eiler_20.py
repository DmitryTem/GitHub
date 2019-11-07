

def factorial(n):
    if n==1:
        return n
    return n*factorial(n-1)


L=list(str(factorial(100)))
print(L)
result=0
print(L)
for i in L:
    result += int(i)
print(result)