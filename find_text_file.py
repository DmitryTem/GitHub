import os 



words = [ 'ОТКАЗ', '36','77']
words = [ 'void convert','void lpArg1']

route = '/home/dmitry/work/'
files = os.walk(route)



for i in files:
  for j in i[2]:
    f = open(i[0]+'/'+j, 'r', encoding = 'cp1251', errors = 'ignore')
    k = 0
    for line in f:
      k += 1
      for word in words:
        res = line.find(word)
        if res > 0:
          print('Route: %s \nNumber of string: %d. Position: %d, %s----Word: %s' %(i[0]+'/'+j,k, res, line , word))
          print('-'*150)
    f.close 
  
 