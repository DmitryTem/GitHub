
import vk_api
import datetime
#import random
from vk_api.longpoll import VkLongPoll, VkEventType



def symbol(string):
    true_symbol=['0','1','2','3','4','5','6','7','8','9','.']
    flag = True
    if string.find('.') == -1: flag = False
    for i in string:
        if i not in true_symbol:
            flag = False
    if flag:
        date_list = string.split('.')
        day = int(date_list[0])
        month = int(date_list[1])
        if day > 31 or month > 12 or month < 7:
            flag = False
    return flag


def date_correct(string):
    if len(string) == 5:
        return string.replace(".", "") + "2019"
    else:
        date_list = string.split('.')
        if len(date_list[0]) == 1: date_list[0] = '0'+date_list[0]
        if len(date_list[1]) == 1: date_list[1] = '0'+date_list[1]
        return date_list[0] + date_list[1] + "2019"
    return


datebeg = datetime.date(2019, 7, 24) # Дата выходного перед первым рабочим днем
weak_list = ['неделя', 'нед', 'Неделя', 'Нед', 'Нед','Н','н']
month_list = ['Месяц','мес','месяц','Мес', 'м','М']
today_list = ['c','C','с','С']
name_of_day = {1:'пн.',2:'вт.',3:'ср.',4:'чт.',5:'пт.',6:'сб.',7:'вскр.'}
datedict = {}

#Сбой в расписании на определенный период
sh_status = True
sh_break_1 = datetime.date(2019, 8, 1)
sh_break_2 = datetime.date(2019, 8, 15)
delta = 2

a = "Вариант 1"
b = "Вариант 2"
c = "Вариант 3"
d = "Вариант 4"

days_in_period = abs((datetime.date(2020, 12, 31) - datebeg).days)
i = 0
while i < days_in_period:
    datedict[i+1] = a
    datedict[i+2] = b
    datedict[i+3] = c
    datedict[i+4] = d
    i = i + 4

token_vk = '269502ac48f4393247fa187cdf996b2be666dee67c48ccddb700c7c837d104bdda542e814bf0fd5f840f9'  # здесь вы должны написать свой access_token

vk_session = vk_api.VkApi(token = token_vk)

longpoll = VkLongPoll(vk_session)
vk = vk_session.get_api()

for event in longpoll.listen():
    if event.type == VkEventType.MESSAGE_NEW and event.to_me and event.text:
        if event.text in weak_list:
            today = datetime.datetime.date(datetime.datetime.today())
            weak_schedule = 'Расписание на неделю: \n'

            for i in range (0,7):
                weak_day = today + datetime.timedelta(days=i)
                k = datetime.datetime.isoweekday(weak_day)
                days_diff = abs((weak_day - datebeg).days)
                if sh_status:
                    if weak_day >= sh_break_1 and weak_day <= sh_break_2:
                        print('Изменения в расписании.')
                        days_diff = days_diff + delta
                weak_schedule += str(weak_day.day) +'.'+ str(weak_day.month) + ' ('+ name_of_day[k] +') ' + str(datedict[days_diff])  + '\n'
            if event.from_user:  # Если написали в ЛС
                print('Запрос расписания на неделю.')
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=weak_schedule
                )

        elif event.text in today_list:
            today = datetime.datetime.date(datetime.datetime.today())
            weak_schedule = ''
            k = datetime.datetime.isoweekday(today)
            days_diff = abs((today - datebeg).days)
            if sh_status:
                if today >= sh_break_1 and today <= sh_break_2:
                    days_diff = days_diff + delta
            weak_schedule += 'Сегодня '+ str(today.day) +'.'+ str(today.month) + ' ('+ name_of_day[k] +') ' + str(datedict[days_diff])  + '\n'
            if event.from_user:  # Если написали в ЛС
                print('Запрос графика на сегодня.')
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=weak_schedule
                )

        elif 3 < len(event.text) < 6 and symbol(event.text):
            mes_str = date_correct(event.text)
            print(mes_str)
            mes_date = datetime.datetime.strptime(mes_str, "%d%m%Y").date()
            print(mes_date)
            days_diff = abs((mes_date - datebeg).days)
            if sh_status:
                if mes_date >= sh_break_1 and mes_date <= sh_break_2:
                    print('Изменения в расписании.')
                    days_diff = days_diff + delta
            if event.from_user and days_diff > 0:  # Если написали в ЛС
                print('Ответ на дату')
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message=str(datedict[days_diff])
                )
        else:
            if event.from_user:  # Если написали в ЛС
                print('Дата введена неверно.')
               # rnd = random.randint(0,9)
                vk.messages.send(  # Отправляем сообщение
                    user_id=event.user_id,
                    random_id=event.random_id,
                    message='Введи дату в формате: 26.07 (число.месяц) \nБуква "с" - график на сегодня \nБуква "н" - расписание на неделю'
                )


