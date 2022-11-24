from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status
from .data.weather_data import get_weather_data
from .data.activity_data import get_activity_data
from .models import Day
from .serializers import DaySerializer


# Create your views here.


def find_letter(location, char):
    index = location.rfind(char)
    second_letter_to_capitalize = index + 1
    string_list = list(location)
    letter_upper = string_list[second_letter_to_capitalize].upper()
    string_list[second_letter_to_capitalize] = letter_upper
    location = "".join(string_list)
    return location


@api_view(['GET', 'POST'])
def get_new_data(request, location, format=None):
    if request.method == 'GET':
        if location[0].islower():
            location = location.capitalize()
        if " " in location:
            location = find_letter(location, " ")
        if "-" in location:
            location = find_letter(location, "-")

        forecast = get_weather_data(location)
        response = get_activity_data(forecast)

        week_data = []

        for i in range(len(response)):
            day_data_dict = {"day": response[i][0], "location": location, "weather": response[i][1],
                             "activity": response[i][2]}
            week_data.append(day_data_dict)

        return Response(week_data)


@api_view(['GET', 'DELETE'])
def days_data_list(request, format=None):
    if request.method == 'GET':
        days = Day.objects.all()
        serializer = DaySerializer(days, many=True)
        return Response(serializer.data)

    elif request.method == 'DELETE':
        Day.objects.all().delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


@api_view(['POST'])
def new_day(request):
    if request.method == 'POST':
        serializer = DaySerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


@api_view(['GET', 'PUT', 'DELETE'])
def day_data(request, id, format=None):
    try:
        day = Day.objects.get(pk=id)
    except Day.DoesNotExist:
        return Response(status=status.HTTP_404_NOT_FOUND)

    if request.method == 'GET':
        serializer = DaySerializer(day)
        return Response(serializer.data)

    elif request.method == 'PUT':
        serializer = DaySerializer(day, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    elif request.method == 'DELETE':
        day.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)
