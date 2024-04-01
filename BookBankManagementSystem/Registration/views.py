from django.shortcuts import render,redirect
from django.contrib.auth.models import User
from django.contrib.auth import authenticate
from django.contrib.auth import login as auth_login
from django.contrib.auth import logout as auth_logout
from django.contrib import messages
from Registration.models import *
from Books.models import *

def index(request):
    current_admin_user = request.user
    current_admin_customer = Customer.objects.get(uid=current_admin_user)
    params={'current_admin_user' : current_admin_user,
                    'current_admin_customer' : current_admin_customer,
                    'departments' : departments,
                    'semesters' : semesters,
                    'customer_type' : customer_type}
    return render(request,'Registration/index.html', params)
def register(request):
    if request.method == "POST":
        usertype = request.POST['usertype']
        username = request.POST['username']
        email = request.POST['email']
        userid = request.POST['userid']
        password = request.POST['password']
        confirm_password = request.POST['confirm_password']
        params_for_password = {'reenter_confirm_password' : True,
             'username' : username,
             'usertype' : usertype,
             'userid' : userid,
             'email' : email,
             'password' : password}
        if usertype == "select":
            messages.error(request,'user type not selected')
            return redirect('register')
        if len(User.objects.filter(username = username)) != 0:
            messages.error(request, 'Username Already Used by Another User Please Give a Different Username')
            return redirect('register')
        if len(Customer.objects.filter(cid = userid)) != 0:
            messages.error(request, 'Userid Already Used by Another User Please Give a Different Userid')
            return redirect('register')
        if usertype == customer_type[0] and len(Customer.objects.filter(type = customer_type[0])) != 0:
            messages.error(request, 'Cannot register as librarian, Librarian already registered')
            return redirect('register')
        if password != confirm_password:
            messages.error(request, 'passwords did not match')
            return render(request, 'Registration/registerPage.html', params_for_password)
        current_user=User.objects.create_user(username=username,email=email,password=password)
        current_customer=Customer.objects.create(cid=userid,uid=current_user,type=usertype)
        current_customer.save()
        current_user.save()
        messages.success(request, 'You have Registered successfully')
        return redirect('login')
    params={'customer_types' : customer_type}
    return render(request, 'Registration/registerPage.html', params)

def login(request):
    if request.method == "POST":
        usertype = request.POST['usertype']
        username = request.POST['username']
        password = request.POST['password']
        current_admin_user = authenticate(username=username,password=password)
        current_admin_customer = Customer.objects.filter(type=usertype,uid=current_admin_user)
        if usertype == 'select':
            messages.error(request, f'User type not selected')
            return redirect('login')
        if len(current_admin_customer)!=1:
            messages.error(request, f'There is no {usertype} with Given username')
            return redirect('login')
        if current_admin_user:
            auth_login(request,current_admin_user)
            messages.success(request,'You are logged in successfully')
            return redirect('index')
        else:
            messages.error(request, 'Given Username not yet registered')
            return redirect('login')
    params={'customer_types' : customer_type}
    return render(request, 'Registration/loginPage.html',params)
def logout(request):
    auth_logout(request)
    messages.success(request, 'You are logged out successfully')
    return redirect('home')
