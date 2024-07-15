import requests


def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Use 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()


def display_weather(data):
    if data.get('cod') != 200:
        print("Error fetching weather data:", data.get('message'))
        return

    city = data['name']
    temperature = data['main']['temp']
    humidity = data['main']['humidity']
    weather = data['weather'][0]['description']

    print(f"Weather in {city}:")
    print(f"Temperature: {temperature}°C")
    print(f"Humidity: {humidity}%")
    print(f"Condition: {weather}")


def main():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    location = input("Enter a city name or ZIP code: ")
    weather_data = get_weather(api_key, location)
    display_weather(weather_data)


if __name__ == "__main__":
    main()
