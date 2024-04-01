from django.urls import path
from Books.views import *

urlpatterns = [
    path('addNewBooks/', addNewBooks, name = 'addNewBooks'),
    path('addExistingBooks/', addExistingBooks, name = 'addExistingBooks'),
    path('issueBook/', issueBook, name = 'issueBook'),
    path('collectBook/', collectBook, name = 'collectBook'),
    path('myDues/', myDues, name = 'myDues'),
    path('viewDues/', viewDues, name = 'viewDues'),
    path('availableBooks/', availableBooks, name = 'availableBooks'),
]
