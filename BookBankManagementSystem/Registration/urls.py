from django.urls import path,include
from Registration.views import *
urlpatterns = [
    path('index/', index, name = 'index'),
    path('index/', include('Books.urls')),
    path('register/', register, name = 'register'),
    path('login/', login, name = 'login'),
    path('logout/', logout, name = 'logout'),

]
