# created by me
from django.contrib import messages
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.models import User
from django.http import HttpResponse
from django.shortcuts import redirect, render

from booktripcrud.models import AdminTours, BookTrip


def home(request):
    return render(request, 'index.html')

def handleLogin(request):
     if request.method == "POST":
        loginUsername = request.POST["loginUsername"]
        loginPassword= request.POST["loginPassword"]

        user=authenticate(username=loginUsername,password=loginPassword)

        if user is not None:
            login(request,user)
            messages.success(request, "Login successfully")
            return redirect('home')
        else:
            messages.error(request, "Invalid credentials, Please try again later")
            return redirect('home')

     return HttpResponse('404-Not found')


def handleLogout(request):
        logout(request)
        messages.success(request,"Logout successfully")
        return redirect('home')


def handleSignup(request):
    if request.method == "POST":
        firstName = request.POST["fName"]
        lastName = request.POST["lName"]
        contact = request.POST["contact"]
        username = request.POST["userName"]
        email = request.POST["email"]
        pass1 = request.POST["pass1"]
        pass2 = request.POST["pass2"]

        # validating form
        if len(username)>10:
            messages.error(request, "username must contain less than 10 character")
            return redirect('home')

        if not username.isalnum():
            messages.error(request, "username must contain only numbers and letters")
            return redirect('home')

        if pass1!=pass2:
            messages.error(request, "password do not match")
            return redirect('home')
        




        # creating user


        myuser = User.objects.create_user(username=username, email=email, password=pass1)
        myuser.first_name = firstName
        myuser.last_name = lastName
        myuser.save()
        messages.success(request, " Your acount has been successfully created")
        return redirect('home')
    else:
        return HttpResponse("404 Not Found")       

def about(request):
    return render (request, 'about.html')

def book(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        address=request.POST['address']
        whereTo=request.POST['location']
        noOfGuest=request.POST['guests']
        arrivalDate=request.POST['arrivals']
        leavingDate=request.POST['leaving']

        contacts=BookTrip(customerName=name,customerEmail=email,customerPhone=phone,customerAddress=address,customerWhereTo=whereTo,customerNoOfGuests=noOfGuest,customerArrivalDate=arrivalDate,customerLeavingDate=leavingDate)
        contacts.save() 

        messages.success(request,'Your request has been submitted successfully our agency will contact you for further procedure')

    return render(request,'book.html')

def package(request):
    packages=AdminTours.objects.all()
    params={'packages':packages}
    return render(request,'package.html',params)

def services(request):
    return render(request, 'services.html')

