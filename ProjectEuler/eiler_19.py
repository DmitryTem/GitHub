import time, sys # В Windows использовать time.clock
import math, datetime, time
if sys.platform[:3] == 'win': 
    timefunc = time.clock 
else: 
    timefunc = time.time # На некоторых платформах Unix дает
			 # лучшее разреше

def find_sunday_count():
    datebeg = datetime.date(1901,1,1)
    dateend = datetime.date(2000,12,31)
    #datebeg = time.strptime("01.01.1901", "%d.%m.%Y")
    #dateend = time.strptime("31.12.2000", "%d.%m.%Y")
    n = 0
    #print(datetime.date.__dict__)
    while datebeg != dateend:
       datebeg += datetime.timedelta(days=1)
       print(datebeg.day)
       if datetime.datetime.weekday(datebeg) == 6 and datebeg.day == 1:
           n += 1 
    print(datebeg,n)
    pass
    return 1
			 
			 
start = timefunc()

#print('Count: %d' %(find_sunday_count()))
print('Count: ', find_sunday_count())
elapsed = timefunc() - start
print(elapsed)



#start = timefunc()
#print('Sum===',find_sum(100000))
#elapsed = timefunc() - start
#print(elapsed)
#print('-'*100)
