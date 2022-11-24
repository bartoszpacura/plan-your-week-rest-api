from requests import get


def get_info_weather(endpoint=""):
    base_url = "https://weatherdbi.herokuapp.com/data/weather/"

    ep = endpoint
    data = get(base_url + ep).json()
    return data


def get_info_activity(endpoint=""):
    base_url = "http://www.boredapi.com/api/activity"

    ep = endpoint
    data = get(base_url + ep).json()
    return data
