from .get_info import get_info_weather
import datetime


def get_weather_data(location):
    data = get_info_weather(location)

    location_weather = data['list']

    forecast = []

    for day_data in location_weather:
        date = day_data['dt_txt']
        year = date[:4]
        month = date[5:7]
        day = date[8:11]

        weather_details = day_data['weather']
        weather_list = weather_details[0]
        weather = weather_list['description']

        if "15:00:00" in date:
            print(date, year, month, day, weather)
            week_day = datetime.date(year=int(year), month=int(month), day=int(day)).weekday()
            days = ["Monday", "Tuesday", "Wednesday", "Thursday", "Friday", "Saturday", "Sunday"]
            forecast.append([days[week_day], weather])

    return forecast
