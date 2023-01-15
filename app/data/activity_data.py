from .get_info import get_info_activity


def get_activity_data(forecast):
    week = []

    for i in range(5):
        day = forecast[i][0]
        weather = forecast[i][1]
        flag = False

        weather_words = ["rain", "shower", "snow", "storm"]
        if any(word in weather for word in weather_words):
            activity_type_endpoint = "?minaccessibility=0&maxaccessibility=0.1"
            flag = True
        else:
            activity_type_endpoint = "?type=social"

        activity_data = get_info_activity(activity_type_endpoint)
        activity = activity_data['activity']

        if flag is True:
            while True:
                activity_words = ["basketball", "football", "volleyball", "outside", "swim", "concert"]
                if any(word in activity for word in activity_words):
                    activity_data = get_info_activity(activity_type_endpoint)
                    activity = activity_data['activity']
                else:
                    break

        week.append([day, weather, activity])

    return week
