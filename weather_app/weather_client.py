import requests # type: ignore

api_key = '152a3375c68bf74bc797b07c22673ed7'

def get_current_weather(city):
        
        current_weather = f'http://api.openweathermap.org/data/2.5/weather?q={city}&appid={api_key}&units=metric'
        response = requests.get(current_weather)
       
        if response.status_code == 200:
            data = response.json()
            current_weather_data = {
                "city_name": data['name'],
                "temperature": data['main']['temp'],
                "weather_condition": data['weather'][0]['description'],
                "humidity_percent": data['main']['humidity'],
                "wind_speed": data['wind']['speed']
            }
            return current_weather_data
        
        else:
            return {'error': f'Error fetching weather data for {city}'}

def get_weather_forecast(city):
        forecast_weather = f'http://api.openweathermap.org/data/2.5/forecast?q={city}&appid={api_key}&units=metric'
        response = requests.get(forecast_weather)

        if response.status_code == 200:
            data = response.json()
            forecast_data = []
            
            for forecast in data['list']:
               forecast_data.append({
                    "temperature": forecast['main']['temp'],
                    "weather_condition": forecast['weather'][0]['description'],
                    "humidity_percent": forecast['main']['humidity'],
                    "wind_speed": forecast['wind']['speed']
            })
            return {
                "city": city,
                "forecast": forecast_data          
            }
        else:
            return {'error': f'Error fetching weather forecast'}