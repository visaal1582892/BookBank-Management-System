from django.urls import path
from Books.views import *

urlpatterns = [
    path('viewBooks/<int:category>/', viewBooks, name = 'viewBooks'),
]
