from .get_info import get_info_weather


def get_weather_data(location):
    data = get_info_weather(location)

    data_list = data['next_days']

    forecast = []

    for i in range(1, 8):
        data_dict = data_list[i]
        weather = data_dict['comment']
        weather = weather.lower()
        day = data_dict['day']
        forecast.append([day, weather])

    return forecast
