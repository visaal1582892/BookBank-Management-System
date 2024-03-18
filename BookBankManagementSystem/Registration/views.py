from django.shortcuts import render
from django.contrib.auth.models import User
from django.contrib.auth import authenticate,login,logout

def index(request):
    return render(request,'Registration.index.html')
def register(request):
    if request.method == "POST":
        pass
