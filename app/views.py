import requests
from django.shortcuts import render

def index(request):
    api_key = '04c72b905504e617d7aed8dabf37d406'
    city = request.GET.get('city')  

    url = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
    response = requests.get(url)
    weather_data = response.json()

    if response.status_code == 200 and 'main' in weather_data:
        context = {
            'city': city,
            'temperature': weather_data['main']['temp'],
            'description': weather_data['weather'][0]['description'],
            'icon': weather_data['weather'][0]['icon'],
            'humidity': weather_data['main']['humidity'],
            'wind_speed': weather_data['wind']['speed'],
            'pressure': weather_data['main']['pressure'],
        }
    else:
        context = {
            'city': city,
            'error': 'Could not retrieve weather data. Please check the city name and try again.'
        }

    return render(request, 'index.html', context)
