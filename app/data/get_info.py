from requests import get


def get_info_weather(city_name=""):

    API_key = "eb39be4e6d7ad03b6e9982268e8be49f"
    base_url = f"http://api.openweathermap.org/data/2.5/forecast?q={city_name}&appid={API_key}"

    data = get(base_url).json()
    return data


def get_info_activity(endpoint=""):
    base_url = "http://www.boredapi.com/api/activity"

    ep = endpoint
    data = get(base_url + ep).json()
    return data
