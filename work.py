import requests
import os
# import simplejson
import re




#s_city = "Kiev, UA"     # name of city and country
# city_id = 703448        # city id of Kiev
appid = os.getenv('TOKEN')

#---------------------------------------------------------------------------------------------------

def help():
    print(
        '----------------------------------------------------------------\n'
        'Лузер, тоесть Юзер!Следуй по инструкции, программа простая.\n'
        'Эта прога ищет для тебя прогноз погоды по городу \n'
        'и по дате с временем  которую ты потом выберешь из\n'
        'предлагаемого списка.\n'
        '----------------------------------------------------------------\n'
        'Мини пошаговая инструкция:\n'
        '----------------------------------------------------------------\n'
        '1. Введи название города в спец формате(Kiev, UA)\n'
        'или цифру из выпадающего списка предложеных городов.\n'
        '2. Выбери и введи дату цифру-ответ из выпадающего списка\n'
        'предложенных дат.\n'
        '3. Выбери и введи цифру ответ с предложеным времинем.\n'
        '4. Получи ответ, дальше или удовлетворись либо пробуй по-новой\n'
        '----------------------------------------------------------------\n '

        ' Если что то не понятно, то мне очень жаль.\n '
        '!!Вдыхни поглубже и давай еще разок!!\n'
    )


#---------------------------------------------------------------------------------------------------

def returned_geolocation_id(s_city):
    '''
    '''
    try:

        res = requests.get("http://api.openweathermap.org/data/2.5/find",
                    params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
        data = res.json()
        cities = ["{} ({})".format(d['name'], d['sys']['country'])
                 for d in data['list']]
        city_id = data['list'][0]['id']

        return city_id

    except Exception as e:
        print("Exception (find):", e)



#---------------------------------------------------------------------------------------------------

def question_location():
    '''Начало программы, приветсвие с выбором города для погоды
    '''
    print('Привет, я могу узнать прогноз погоды для тебя.\n'
          'Напиши ЦИФРУ-ОТВЕТ или ГОРОД СО СТРАНОЙ в формате: Kiev, UA\n'
          '1.) Kiev, UA\n'
          '2.) Lviv, UA\n'
          '3.) Odessa, UA\n'
          '4.) Harkov, UA\n'
          '5.) Yalta, UA\n'
          '6.) Help\n'
          '7.) Да ну его все!'
          )

    while True:
        answer = input('--------input answer --------\n')
        if not answer.isalpha() and not answer.isdigit():
            re_answer = re.findall(r'[A-Z][a-z]+,.[A-Z]{2}', answer)
            if re_answer:
                if str(returned_geolocation_id(re_answer)).isdigit():
                    return re_answer[0]
                    break
                else:
                    print('Wrong name of city or format0!You need: Lviv, UA ')
                    continue

            else:
                print('Wrong name of city or format#!You need: Lviv, UA ')
                continue

        elif answer.isdigit():
            if answer == '1':
                return 'Kiev, UA'
                break
            elif answer == '2':
                return 'Lviv, UA'
                break
            elif answer == '3':
                return 'Odessa, UA'
                break
            elif answer == '4':
                return 'Harkov, UA'
            elif answer == '5':
                return 'Yalta, UA'
            elif answer == '6':
                help()
                continue
            elif answer == '7':
                print('Ну и вали!!!')
                exit()
            else:
                print('Wrong name of city or format!!You need: Lviv, UA ')
                continue

        elif answer == 'exit' or 'EXIT' or 'Exit':
            print('Ну и вали!!!')
            exit()
        else:
            print('input corrected name of city!?You need: Lviv, UA')
            continue

#---------------------------------------------------------------------------------------------------

def get_request():
    '''
    The function sends a request to API openweathermap

    '''

    try:
        # res = requests.get("http://api.openweathermap.org/data/2.5/weather",
        #                    params={'id': question_location(), 'units': 'metric',
        #                            'lang': 'ru', 'APPID': appid})
        res = requests.get("https://api.openweathermap.org/data/2.5/forecast?q={}\
                                &appid={}".format(question_location(), appid))
        data = {}
        data = res.json()


        # print("conditions:", data['weather'][0]['description'])
        # print("temp:", data['main']['temp'])
        # print("temp_min:", data['main']['temp_min'])
        # print("temp_max:", data['main']['temp_max'])
        # print("Weather:", data['weather'][0]['description'])
        # five_days_weather = [pprint.pprint(data)]

        # print(five_days_weather)
        print(data)
    except Exception as e:
        print("Exception (weather):", e)
        pass
    # return print(data)

#---------------------------------------------------------------------------------------------------

get_request()














"""
data = get_request() # заварачиваем в переменную

#-----------------------------------------------------------------------------

def in_json(obj):
    '''Переобразует в читаемый код
    '''
    return simplejson.dumps(obj, indent=2, encoding='utf-8',\
                            iterable_as_array=False)

#-----------------------------------------------------------------------------
def write_all_date():
    all_date = []

    i = 0
    while i < len(data['list']):
        all_date.append(data['list'][i]['dt_txt'])
        i += 1
    return all_date

#-----------------------------------------------------------------------------
calling_date = '2019-04-26 15:00:00'

def find_in_list():
    '''
    Функция исчит похожую дату  и время в листе и при совпадении значения записует
     в переменную copy_data_list
    '''
    i = 0
    while i < len(data['list']):
            # print(type(data['list'][i]['dt_txt']))
            if data['list'][i]['dt_txt'] == calling_date:
                copy_data_list = data['list'][i]
                i += 1
            else:
                i += 1

    return copy_data_list

#------------------------------------------------------------------------------

#print(find_in_list())
#print(str(len(data['list'])) + '.) ' + write_all_date()[0][-8:])
#print(city_id)
question_location()
#print(data['list'][0]['dt_txt'])
#print(data['list'][0]['dt_txt'] == calling_date)

#------------------------------------------------------------------------------

s = 'Kyiv'
etalon = 'Kyiv, UA'

"""