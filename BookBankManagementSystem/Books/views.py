from django.shortcuts import render
from Books.models import *

def viewBooks(request,category):
    current_category=Category.objects.get(cateid=category)
    books=Books.objects.filter(cateid=current_category)
    params = {'category' : category, 'books' : books}
    return render(request,'Books/viewBooks.html',params)
