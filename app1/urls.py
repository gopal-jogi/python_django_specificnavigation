from django.urls import path
from app1.views import *
app_name='first'
urlpatterns = [
    path('index/',index,name='index'),
]