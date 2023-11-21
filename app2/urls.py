from django.urls import path
from app2.views import *

app_name='second'

urlpatterns = [
    path('page/',page,name='page'),
]