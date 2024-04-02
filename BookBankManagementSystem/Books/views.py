from django.shortcuts import render,redirect
from django.contrib import messages
from django.http import HttpResponse
from Books.models import *
from Registration.models import *
import datetime

def addNewBooks(request):
    if request.method == "POST":
        bookName = request.POST['bookName']
        author = request.POST['author']
        description = request.POST['description']
        department = request.POST['department']
        semester = int(request.POST['semester'])
        bookCount = int(request.POST['bookCount'])
        existing_books = Book.objects.filter(bname=bookName, bauthor=author)
        print(department)
        current_department = Department.objects.get(dname=department)
        if len(existing_books) != 0:
            messages.error(request, 'Book Already Existed')
            return redirect('index')
        new_book = Book.objects.create(bname=bookName, bauthor=author, bdescription=description, did=current_department, bsem=semester, bcount=bookCount)
        new_book.save()
        messages.success(request, 'New Book successfully Added')
        return redirect('index')
    return HttpResponse('Nothing')
def addExistingBooks(request):
    if request.method == "POST":
        bookId = int(request.POST['bookId'])
        bookCount = int(request.POST['bookCount'])
        try:
            current_book = Book.objects.get(pk=bookId)
        except Book.DoesNotExist:
            messages.error(request, 'Given BookId does not exist')
            return redirect('index')
        current_book.bcount = current_book.bcount + bookCount
        current_book.save()
        messages.success(request, 'Books successfully Added')
        return redirect('index')
    return HttpResponse('Nothing')
def issueBook(request):
    if request.method == 'POST':
        userId = request.POST['userId']
        bookId = request.POST['bookId']
        try:
            current_student = Customer.objects.get(pk=userId)
            current_book = Book.objects.get(pk=bookId)
        except (Customer.DoesNotExist, Book.DoesNotExist):
            messages.error(request, 'Either given user id or book id does not exist')
            return redirect('index')
        odate = datetime.date.today()
        orders = Order.objects.filter(cid=current_student, bid=current_book, odate=odate)
        if len(orders) != 0:
            messages.error(request, 'order already existed')
            return redirect('index')
        current_book.bcount -= 1
        duedate = odate + datetime.timedelta(days=borrowDays)
        current_order = Order.objects.create(cid=current_student, bid=current_book, odate=odate, duedate=duedate)
        current_order.save()
        current_book.save()
        messages.success(request, 'Book Issued successfully')
        return redirect('index')
    return HttpResponse('Nothing')

def collectBook(request):
    if request.method == 'POST':
        userId = request.POST['userId']
        bookId = request.POST['bookId']
        try:
            current_student = Customer.objects.get(pk=userId)
            current_book = Book.objects.get(pk=bookId)
            current_order = Order.objects.get(cid=current_student, bid=bookId)
        except (Customer.DoesNotExist, Book.DoesNotExist, Order.DoesNotExist):
            messages.error(request, 'Either given user id or book id does not exist or no order registered with Given credentials')
            return redirect('index')
        current_book.bcount += 1
        today = datetime.date.today()
        duedate = current_order.duedate
        if today > duedate:
            messages.info(request, f'Duedate crossed by {today-duedate}')
        current_order.delete()
        current_book.save()
        messages.success(request, 'Book Collected successfully')
        return redirect('index')
    return HttpResponse('Nothing')
def myDues(request):
    myDues = []
    current_customer = Customer.objects.get(uid = request.user)
    my_orders = Order.objects.filter(cid=current_customer)
    today = datetime.date.today()
    for order in my_orders:
        if order.duedate < today:
            myDues.append(order)
    params = {'myDues' : myDues}
    return render(request, 'Books/myDues.html', params)
def viewDues(request):
    dues = []
    today = datetime.date.today()
    for order in Order.objects.all():
        if order.duedate < today:
            dues.append(order)
    params = {'dues' : dues}
    return render(request, 'Books/viewDues.html', params)
def availableBooks(request):
    if request.method == "POST":
        department = request.POST['department']
        semester = int(request.POST['semester'])
        current_department = Department.objects.get(dname=department)
        current_books = Book.objects.filter(did=current_department, bsem=semester)
        params = {"current_books" : current_books, 'departments' : departments, 'semesters' : semesters}
        return render(request, 'Books/availableBooks.html', params)
    params = {'departments' : departments, 'semesters' : semesters}
    return render(request, 'Books/availableBooks.html', params)
