from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .forms import NewUserForm
from django.contrib.auth import login
from django.contrib import messages
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import AuthenticationForm
from books.models import Book

from django.contrib.auth import login, authenticate, logout


def Home(request):
    current_user = request.user
    print(current_user)
    if request.user.is_anonymous:
        current_user=None
    print(current_user)
    
    booksdata=Book.objects.all()
    return render(request,'LMS/main.html',{"books":booksdata,"user":current_user})


def register_request(request):
    # print(" in the form section ")
    if request.method == "POST":
        print("in the post section")
        form = NewUserForm(request.POST)
        if form.is_valid():
            print("in the post fomr is valid    ")
            user = form.save()
            login(request, user)
            messages.success(request, "Registration successful.")
            return redirect("/")
        else:
            # print("form is invalid")
            messages.error(request, form.errors)
            print(form.errors)
            return redirect("/register")
    form = NewUserForm()
    # else:
    #     return HttpResponse("error")
    return render(request=request, template_name="LMS/register.html", context={"register_form": form})


def login_request(request):
	if request.method == "POST":
		form = AuthenticationForm(request, data=request.POST)
		if form.is_valid():
			username = form.cleaned_data.get('username')
			password = form.cleaned_data.get('password')
			user = authenticate(username=username, password=password)
			if user is not None:
				login(request, user)
				messages.info(request, f"You are now logged in as {username}.")
				return redirect("/")
			else:
				messages.error(request, "Invalid username or password.")
				return redirect("/login")

		else:
			messages.error(request, "Invalid username or password.")
	form = AuthenticationForm()
	return render(request=request, template_name="LMS/login.html", context={"login_form": form})


def logout_request(request):
	logout(request)
	messages.info(request, "You have successfully logged out.")
	return redirect("/login")


def Admin(request):
    if request.method == "POST":
        bookname=request.POST['book']
        booktitle=request.POST['title']
        print(bookname,booktitle)
        b=Book(book=bookname,title=booktitle)
        b.save()
        messages.success(request,"book content saved !!!! ")
        return redirect('/upload')
    return render(request, template_name="LMS/admin.html")

def update(request,id):
    if request.method == "POST":
        bookname=request.POST['book']
        booktitle=request.POST['title']
        bookId=Book.objects.get(id=id)
        bookId.book=bookname
        bookId.title=booktitle
        bookId.save()
        messages.success(request,"book content updated !!!! ")
        return redirect('/')
    return render(request, template_name="LMS/admin.html")

def delete(request,id):
    data=Book.objects.get(id=id)
    data.delete()
    messages.success(request,"Book content Deleted !!!! ")
    return redirect('/')
    
