from datetime import datetime
from playsound import playsound



def timefunc(time : str) -> str: # Функция для проверки значений времени
    if len(time) == 8: # Проверка длины строки времени
        if int(time[0:2]) > 23 or int(time[3:5]) > 59 or int(time[6:8]) > 59: # Проверка на правильно введении часов, минут, секунд
            return 'Вы неверно написали часы, минуты или секунды, попробуйте еще раз'
        else:
            return 'Все отлично, класс'

    else:
        return 'Не корректно введено время'



while True:
    time = input('Введите время в формате часы/минуты/секунды: ')
    time1 = timefunc(time)
    if time1 != 'Все отлично, класс': # Если неправильно было что-то введено, ты возвращается где именно человек допустил ошибку
        print(time1)

    else: # Если все окажется верно
        print(f'Отлично, будильник установлен на время {time}')
        break

hour = int(time[0:2])
minute = int(time[3:5])
second = int(time[6:8])

while True:
    now_time = datetime.now()

    now_hour = now_time.hour
    now_min = now_time.minute
    now_sec = now_time.second

    if now_hour == hour:
        if now_min == minute:
            if now_sec == second:
                print('Пора просыпаться, друг мой')
                playsound('Здесь вы пишите путь к муз.файлу')
                break




