# Main Program Execution
from weather_app.weather_client import get_current_weather, get_weather_forecast

def main():
    city_names = input("Enter one or more City Names separated by space: ").split()
    choice = input("Choose an option: ") # 1 to display Current Weather data while 2 to display a 5-day forecast
    
    for city in city_names:
        if choice == "1":
          result = get_current_weather(city)
          print(result)

        elif choice == "2":
          result = get_weather_forecast(city)
          print(result)

        else:
          print('Invalid input. Insert either 1 or 2')

if __name__ == "__main__":
    main()