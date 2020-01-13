import time
import datetime 
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.expected_conditions import presence_of_element_located

with webdriver.Chrome('/Users/dmitryt/.../chromedriver') as driver:
    driver.get('https://site/sign')
    uname = driver.find_element_by_css_selector("input#usName_1.__input")
    uname.click()
    uname.send_keys('...@y....ru')
    upass = driver.find_element_by_css_selector("input#pswrd_2.__input")
    upass.click()
    upass.send_keys('')
    submit = driver.find_element_by_css_selector("button.__button.button._theme_primary._size_normal.index_textAlignCenter_2zmzz._fluid")
    submit.click()
    time.sleep(1)
    driver.get('https://site/products?filter=all')
    time.sleep(5)
    value = driver.find_elements_by_css_selector("td")
    length = len(value)
    nrow = length//14
    ncol = 14
    buf = list()
    time.sleep(5)
    for i in range(length):
        buf.append(value[i].text)
    
    ds = {"checkbox":pd.Series(buf[0:length:14]),
     "art": pd.Series(buf[1:length:14]),
     "img": pd.Series(buf[2:length:14]),
     "barcode": pd.Series(buf[3:length:14]),
     "name": pd.Series(buf[4:length:14]),
     "date": pd.Series(buf[5:length:14]),
     "status": pd.Series(buf[6:length:14]),
     "view": pd.Series(buf[7:length:14]),
     "storage": pd.Series(buf[8:length:14]),
     "commission": pd.Series(buf[9:length:14]),
     "price": pd.Series(buf[10:length:14]),
     "price_before_discount": pd.Series(buf[11:length:14]),
     "price_with_premium": pd.Series(buf[12:length:14]),
     "action": pd.Series(buf[13:length:14]),
     }
    
    df = pd.DataFrame(ds)
    
    time_values = dict()
    for i in range(7):
        code = df.barcode[i].split('ST')[1]
        driver.get('https://site/page/detail/id/{}/'.format(code))
        time.sleep(3)
        t = driver.find_elements_by_css_selector("time")
        if t: 
            temp = [t[i].text for i in range(len(t))]
            time_values[code] = temp

month = {'Января': '01',
      'Февраля': '02',
      'Марта': '03',
      'Апреля': '04',
      'Мая': '05',
      'Июня': '06',
      'Июля': '07',
      'Августа': '08',
      'Сентября': '09',
      'Октября': '10',
      'Ноября': '11',
      'Декабря': '12',   
     }
today = datetime.datetime.today().date()

new_comment_list = list()
if time_values:
    for i in time_values:
        for j in range(len(time_values[i])):
            for k,v in month.items():
                time_values[i][j] = (time_values[i][j].replace(k,v)).replace(' ','.')
            delta = today - datetime.datetime.strptime(time_values[i][j], '%d.%m.%Y').date()
            delta_int = int(str(delta).split()[0])
            if delta_int > 1:
                new_comment_list.append(i)

            
if new_comment_list:
    ncl = set(new_comment_list)
    msg = 'Hey! New comments appeared: \n'
    for i in ncl:
        msg = msg + 'https://site/.../detail/id/{}/ \n'.format(i)

    print(msg)
