import time, sys, math, collections # В Windows использовать time.clock
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

def number_into_str(k):
    s = ''
    num_20 = {'1':"one",'2':"two",'3':"three",'4':"four",'5':"five",'6':"six",'7':"seven",'8':"eight",'9':"nine",
                 '10':"ten",'11':"eleven",'12':"tweleve",'13':"thirteen",'14':"fourteen",'15':"fifteen",'16':"sixteen",'17':"seventeen",'18':"eighteen",'19':"nineteen"}
    half = {'20':"twenty",'30':"thirty",'40':"forty",'50':"fifty",'60':"sixty",'70':"seventy",'80':"eighty",'90':"ninety"}
    
    for i in range(1,k+1):
        test = ''
        if i < 20:
           # print('1-19')
            s += num_20[str(i)]
            test += num_20[str(i)]
        elif i > 19 and i < 100:
           # print('20-99',i)
            j=i%10
            if j==0:
                s += half[str(i)]
                test += half[str(i)]
            else: 
                s += half[str(i-j)] + num_20[str(j)]
                test += half[str(i-j)] + num_20[str(j)]
        elif i > 99 and i < 1000:
         #   print('99-1000', i)
            k=i%100
            if k != 0:
                s+= num_20[str(i//100)] + 'hundredand'
                test += num_20[str(i//100)] + 'hundredand'
                if i%100 < 20:
                    s+= num_20[str(i%100)]
                    test += num_20[str(i%100)]
                else:
                    if i%10==0:
                        s+= half[str(i%100)]
                        test += half[str(i%100)]
                    else: 
                        s += half[str((i%100)-(i%10))] + num_20[str(i%10)]
                        test += half[str((i%100)-(i%10))] + num_20[str(i%10)]
            else:
                s+= num_20[str(i//100)] + 'hundred'
                test += num_20[str(i//100)] + 'hundred'
        elif i>999:
            s+= 'onethousand'
        else: s += '-'
        print(test)
    return s
			 
			 
start = timefunc()

print('Main===',len(number_into_str(1000)))
elapsed = timefunc() - start
print(elapsed)



#start = timefunc()
#print('Sum===',find_sum(100000))
#elapsed = timefunc() - start
#print(elapsed)
#print('-'*100)




  