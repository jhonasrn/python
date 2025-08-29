# weather_client.py
import requests
import os

class WeatherAPI:
    def __init__(self, api_key=None):
        self.api_key = api_key or os.getenv('WEATHER_API_KEY')
        self.base_url = "http://api.openweathermap.org/data/2.5/weather"
    
    def get_weather(self, city_name):
        params = {
            'q': city_name,
            'appid': self.api_key,
            'units': 'metric',
            'lang': 'en'
        }
        
        try:
            response = requests.get(self.base_url, params=params)
            data = response.json()
            
            if response.status_code == 200:
                self.display_weather(data, city_name)
            else:
                print(f"Error: {data.get('message', 'Unknown error')}")
                
        except requests.RequestException as e:
            print(f"Network error: {e}")

    def display_weather(self, data, city_name):
        print(f"\n🌤️ Weather in {city_name}:")
        print(f"Temperature: {data['main']['temp']}°C")
        print(f"Condition: {data['weather'][0]['description'].title()}")
        print(f"Humidity: {data['main']['humidity']}%")
        print(f"Wind Speed: {data['wind']['speed']} m/s")

def main():
    api_key = "your_api_key_here"  # Get from openweathermap.org
    weather = WeatherAPI(api_key)
    
    city = input("Enter city name: ")
    weather.get_weather(city)

if __name__ == "__main__":
    main()