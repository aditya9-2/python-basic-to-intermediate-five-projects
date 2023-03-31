import requests
import json
import win32com.client as wincom

speak = wincom.Dispatch("SAPI.SpVoice")

city = input("Enter the name of the city: ")

url = f"https://api.weatherapi.com/v1/current.json?key=366ad543683f40f9b30191246233003&q={city}"

r = requests.get(url)
# print(r.text)
weatherDic = json.loads(r.text)

# Keywords to fetch json file's particular report
temp = weatherDic["current"]["temp_c"]
predictableWeather = weatherDic["current"]["condition"]["text"]
feelsLike = weatherDic["current"]["feelslike_c"]
wind = weatherDic["current"]["wind_kph"]
humid = weatherDic["current"]["humidity"]

speak.Speak(f" Currently the Temperature of {city} is {temp} degrees, feels like{feelsLike} degrees. predictable "
            f"weather is {predictableWeather}, wind is {wind} kilometer per hour and humidity is {humid}")

