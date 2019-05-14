import requests
import os
import re
import pprint

# appid = '0fb87e9c7207bb8b3d51cb647269f5c9'
#s_city = "Kiev, UA"     # name of city and country
# city_id = 703448        # city id of Kiev

appid = os.getenv('TOKEN')

#---------------------------------------------------------------------------------------------------

def help():
    print(
        '----------------------------------------------------------------\n'
        'Лузер, то есть Юзер!Следуй по инструкции, программа простая.\n'
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
        '3. Выбери и введи цифру ответ с предложенным временем.\n'
        '4. Получи ответ, дальше или удовлетворись либо пробуй по-новой\n'
        '5. Для выхода напиши в ответе exit'
        '----------------------------------------------------------------\n '

        ' Если что то не понятно, то мне очень жаль.\n '
        '!!Вдохни поглубже и давай еще разок!!\n'
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
          'P.S.Если ты будешь писать название города то не забудь то что\n'
          'оно должно быть написано англ. буквами как в оригинале\n'
          'Если это украинский город, то не Lvov а Lviv.\n\n'
          '1.) Kiev, UA\n'
          '2.) Lviv, UA\n'
          '3.) Odessa, UA\n'
          '4.) Kharkov, UA\n'
          '5.) Yalta, UA\n'
          '6.) Help\n'
          '7.) Да ну его все!'
          )

    while True:
        answer = input('-------------------------input answer ----------------------------\n')
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
                return 'Kharkiv, UA'
                break
            elif answer == '5':
                return 'Yalta, UA'
                break
            elif answer == '6':
                help()
                continue
            elif answer == '7':
                print('Ну и вали!!!')
                exit()
            else:
                print('Wrong name of city or format!!You need: Lviv, UA ')
                continue

        elif answer == 'exit':
            print('Ну и вали!!!')
            exit()
        else:
            print('input corrected name of city!?You need: Lviv, UA')
            continue

s_city = question_location()
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
                                &appid={}".format(s_city, appid))
        data = {}
        data = res.json()


        # print("conditions:", data['weather'][0]['description'])
        # print("temp:", data['main']['temp'])
        # print("temp_min:", data['main']['temp_min'])
        # print("temp_max:", data['main']['temp_max'])
        # print("Weather:", data['weather'][0]['description'])
        # five_days_weather = [pprint.pprint(data)]

        # pprint.pprint(data)




    except Exception as e:
        print("Exception (weather):", e)
        pass
    return data


data = get_request()
#---------------------------------------------------------------------------------------------------

def new_dict():
    DT_txt = {}
    for index, value in enumerate(data['list']):
        for key, val in value.items():
            if key == 'dt_txt':
                DT_txt[val] = {}
                DT_txt[val].update({'pozition': index})

    for index, value in DT_txt.items():
        DT_txt[index].update({'clouds': data['list'][DT_txt.get(index).get('pozition'
                                                                           )].get('clouds').get('all')})
        DT_txt[index].update({'humidity': data['list'][DT_txt.get(index).get('pozition'
                                                                             )].get('main').get('humidity')})
        DT_txt[index].update({'temp': data['list'][DT_txt.get(index).get('pozition'
                                                                         )].get('main').get('temp')})

        DT_txt[index].update({'weather': data['list'][DT_txt.get(index).get('pozition'
                                                                            )].get('weather')[0].get('description')})
        DT_txt[index].update({'wind': data['list'][DT_txt.get(index).get('pozition'
                                                                         )].get('wind').get('speed')})
        DT_txt[index].update({'dt': index})

    return DT_txt

new_dict = new_dict()
#----------------------------------------------------------------------------------------------------------------------

def questions_time():
    '''
    '''
    print('Я тебя понял, есть такой город как {0}.\n\n'
          'Теперь давай выбери дату и время с прогнозом\n'
          'из этого огромного списка.\n\n'
          'Если ты готов его увидить,\n'
          'то жми ENTER.\n'.format(re.findall('([A-Za-z]+),',s_city)[0]))

    answer_to_contin = input('-------------------------input answer ----------------------------\n')
    if answer_to_contin or not answer_to_contin:

        for index, value in enumerate(new_dict.items()):
            print(str(index + 1) + ').',value[0])
        print('------------------------------------------------------------------\n\n')
        while True:
            print('И снова я ожидаю от тебя ЦИФРУ-ОТВЕТ:\n\n'
                  'Которая в диапазоне данного списка.\n')
            answer_the_time = input('-------------------------input answer ----------------------------\n')
            time_dict = {}
            if answer_the_time.isdigit():
                for index, value in enumerate(new_dict.items()):
                    time_dict.update({index + 1: value[0]})

                if time_dict.get(int(answer_the_time)):
                    td = time_dict.get(int(answer_the_time))
                    break
            elif answer_the_time == 'exit':
                exit()
            else:
                continue
    elif answer_to_contin == 'exit':
        exit()

    return td

questions_time = questions_time()


#-----------------------------------------------------------------------------------------------------------
def weather_to_screen(arg):
    print('\nИ так прогноз погоды на {0}!\n'
          'Небо будет на {1} % покрыто облаками.\n'
          'И как сказал бы англичанин:\n'
          '"And in general, at this time the weather will be {2}"\n'
          'Влажность воздуха {3} %\n'
          'А на термометрах обесчают {4} C*\n'
          'Скорость ветра будет {5} м/с\n'
          'На этом все!\n'.format(
        arg.get('dt'),
        arg.get('clouds'),
        arg.get('weather'),
        arg.get('humidity'),
        int(arg.get('temp')) - 273,
        arg.get('wind')
    ))
    exit()



#------------------------------------------------------------------------------------------------------






"""

TOKEN=0fb87e9c7207bb8b3d51cb647269f5c9
"""