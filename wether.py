__author__ = 'Владелец'


import requests
import os

s_city = "Kiev, UA"
city_id = 703448
appid = os.getenv("TOKEN")
try:
   res = requests.get("http://api.openweathermap.org/data/2.5/find",
                params={'q': s_city, 'type': 'like', 'units': 'metric', 'APPID': appid})
   data = res.json()
   cities = ["{} ({})".format(d['name'], d['sys']['country'])
             for d in data['list']]
   print("city:", cities)
   city_id = data['list'][0]['id']
   print('city_id=', city_id)
except Exception as e:
   print("Exception (find):", e)



# try:
#     res = requests.get("http://api.openweathermap.org/data/2.5/weather",
#                  params={'id': city_id, 'units': 'metric', 'lang': 'ru', 'APPID': appid})
#     data = res.json()
#     print("conditions:", data['weather'][0]['description'])
#     print("temp:", data['main']['temp'])
#     print("temp_min:", data['main']['temp_min'])
#     print("temp_max:", data['main']['temp_max'])
# except Exception as e:
#     print("Exception (weather):", e)
#     pass



