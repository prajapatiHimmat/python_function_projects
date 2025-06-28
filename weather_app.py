import requests

API_KEY = "f150fa5b69f79744f6c7b7b746d7af48"

def get_weather(city):
    url = f"https://api.openweathermap.org/data/2.5/weather?q={city}&appid={API_KEY}&units=metric"
    response = requests.get(url)

    if response.status_code == 200:
      data = response.json()
      temp = data['main']['temp']
      condition = data['weather'][0]['description']

      if "clear" in condition:
         emoji = "☀️"
      elif "cloud" in condition:
         emoji = "☁️"
      elif "rain" in condition:
         emoji ="🌧️"
      elif "snow" in condition:
         emoji = "❄️"
      elif "storm" in condition or "thunder" in condition:
         emoji = "⛈️"
      else:
         emoji = "🌡️"

      output = (
         f"\nweather in {city.title()}:\n"
         f"Temperature: {temp}°C\n"
         f"{emoji}  condition : {condition.title()}\n"
         f"------------------------------\n"

      )

      print(output)

      with open("weather_history.txt" , "a" , encoding="utf-8") as file:
        file.write(output)

    else:
       print("city not found or error in fetching data.")


def menu():
   print("=== Weather App ===")
   city = input("Enter city name: ")
   get_weather(city)


menu()