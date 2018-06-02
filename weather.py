import requests
import json


params = {'APPID': 'e2b39a3577415e6590259d3aa91af4fe',
            'lat': 35, 'lon': 139}

weather = requests.get('https://api.openweathermap.org/data/2.5/weather', params=params)

weather_dict = weather.json()

#weather description
print weather_dict['weather'][0]['description']
#temperature
print "temp: {} humidity: {}".format(weather_dict['main']['temp'], weather_dict['main']['humidity'])

