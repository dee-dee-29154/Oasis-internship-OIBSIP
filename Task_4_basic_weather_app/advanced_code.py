import tkinter as tk
import requests


def get_weather(api_key, location):
    base_url = "http://api.openweathermap.org/data/2.5/weather"
    params = {
        'q': location,
        'appid': api_key,
        'units': 'metric'  # Change to 'imperial' for Fahrenheit
    }
    response = requests.get(base_url, params=params)
    return response.json()


def display_weather():
    api_key = "YOUR_API_KEY"  # Replace with your OpenWeatherMap API key
    location = location_entry.get()
    weather_data = get_weather(api_key, location)

    if weather_data.get('cod') != 200:
        result_label.config(text="Error: " + weather_data.get('message'))
        return

    city = weather_data['name']
    temperature = weather_data['main']['temp']
    humidity = weather_data['main']['humidity']
    weather = weather_data['weather'][0]['description']

    result_label.config(
        text=f"Weather in {city}:\nTemperature: {temperature}°C\nHumidity: {humidity}%\nCondition: {weather}")


# Setting up the GUI
app = tk.Tk()
app.title("Weather App")

tk.Label(app, text="Enter City Name or ZIP Code:").pack()
location_entry = tk.Entry(app)
location_entry.pack()

get_weather_button = tk.Button(app, text="Get Weather", command=display_weather)
get_weather_button.pack()

result_label = tk.Label(app, text="")
result_label.pack()

app.mainloop()
