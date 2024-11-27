from django.urls import path
from . import views

urlpatterns = [
    path("get-current-chromosome/", views.getCurrentTimeTable, name="get_chromosomes"),
    path("get-historical-timetables/", views.getHistoricalTimeTable, name="get_historical")
]
