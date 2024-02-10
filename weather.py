from dotenv import load_dotenv
from pprint import pprint
import requests
import os

load_dotenv()


def get_current_weather(city="Qiryat Ono"):
    request_url = f'https://api.openweathermap.org/data/2.5/weather?&appid={os.getenv("API_KEY")}&q={city}&units=metric'
    weather_data = requests.get(request_url).json()
    print(request_url)
    return weather_data


if __name__ == "__main__":
    city = input("enter city")
    weather_json = get_current_weather(city)
    pprint(weather_json)
