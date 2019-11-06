import numpy as np
import re
import urllib.request
from bs4 import BeautifulSoup


def get_html(url):
    response = urllib.request.urlopen(url)   
    return response.read()                   


def parse(text):
    soup = BeautifulSoup(text, features="html.parser")
    table = soup.find('table', class_='data')
    temp = []
    daily_return = []
    for row in table.find_all('tr')[2:]:
        cols_date = row.find_all('td')[0].string
        cols_rate = float(re.sub(r',', '.', row.find_all('td')[2].string))
        temp.append({'date': cols_date,
                     'rate': cols_rate
                     })
    n = len(temp)-1
    daily = np.zeros(n)
    for i in range(n):
        daily[i] = temp[i+1]['rate'] - temp[i]['rate'] #получили ряд дневных

    monthly = daily.std()
    ror_mean = (1. + daily).mean()
    yearly = np.sqrt((monthly**2 + ror_mean**2)**12 - ror_mean**24)

    years_total = daily.size/2
    carg = (daily[-1] + 1.) ** (1 / years_total) - 1

    print('Mean: %f' %yearly)
    print('Standard deviation: %f' %carg)


def main(s_date_from = '17.09.2019', s_date_to = '24.09.2019', s_code = 'R01235'):
    parse(get_html('https://www.cbr.ru/currency_base/dynamics/?UniDbQuery.Posted=True&UniDbQuery.mode=1&UniDbQuery.date_req1=&UniDbQuery.date_req2=&UniDbQuery.VAL_NM_RQ=' +s_code+ '&UniDbQuery.FromDate=' + s_date_from +'&UniDbQuery.ToDate='+ s_date_to))


print('USD')
main('01.01.2018', '31.12.2018', 'R01235') # usd

print('Euro')
main('01.01.2018', '31.12.2018', 'R01239') # eur