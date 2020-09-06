from django.urls import include, path
from rest_framework import routers
from . import views
urlpatterns = [
    path('create/', views.viewCreateCalendar, name='create'),
    path('hola/', views.viewTest, name='hola')
    ]