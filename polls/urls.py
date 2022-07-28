from django import views
from django.urls import path
from . import views


urlpatterns = [
    path('aashay/',views.index,name='index')
]
