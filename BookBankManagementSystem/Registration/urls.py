from django.urls import path,include
from Registration.views import *
urlpatterns = [
    path('index/', index, name = 'index'),
    path('register/', register, name = 'register')
]
