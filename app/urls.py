from django.urls import path
from . import views
from rest_framework.urlpatterns import format_suffix_patterns

urlpatterns = [
    path('<str:location>', views.get_new_data, name="get_new_data"),
    path('days/list/', views.days_data_list, name="days_data_list"),
    path('days/list/new/', views.new_day, name="new_day"),
    path('days/list/<int:id>', views.day_data, name="day_data"),
]

urlpatterns = format_suffix_patterns(urlpatterns)
