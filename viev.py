import datetime

def greetings():
    now = datetime.datetime.now()
    now = int('%d' % now.hour)
    if now < 6:
        return print('Доброй ночи!')
    elif 6 <= now < 11:
        print('Доброе утро!')
    elif 11 <= now < 17:
        print('Добрый день!')
    else:
        print('Добрый вечер!')
        
greetings()        
