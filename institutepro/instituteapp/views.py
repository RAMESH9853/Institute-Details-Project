from django.shortcuts import render,redirect
from .models import Course
from .models import ContactForm,feedbackData
from django.http import HttpResponse
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required
from .forms import RegistrationForm
import datetime
date1 = datetime.datetime.now()


@login_required(login_url='loginpage')
def HomePage(request):
    return render(request,'homepage.html')

@login_required(login_url='loginpage')
def ContactPage(request):
    if request.method == 'GET':
        return render (request,'contactpage.html')
    else:     #POST
        ContactForm(
            first_name = request.POST['fname'],
            last_name = request.POST['lname'],
            email = request.POST['email'],
            mobile = request.POST['mobile'],
            course = request.POST['course'],
            location = request.POST['location'],
        ).save()

    return render(request,'contactpage.html')

@login_required(login_url='loginpage')
def ServicePage(request):
    course = Course.objects.all()
    return render(request,'servicepage.html',{'course':course})

@login_required(login_url='loginpage')
def FeedbackPage(request):
    if request.method == 'GET':
        data = feedbackData.objects.all().order_by('-id')
        return render(request,'feedbackpage.html',{'data':data})
    else:
        feedbackData(
        content = request.POST['feedback'],
        user_name=request.POST['user'],
        date = date1
        ).save()
        data = feedbackData.objects.all().order_by('-id')
        return render(request,'feedbackpage.html',{'data':data})
  

@login_required(login_url='loginpage')
def GalleryPage(request):
    return render(request,'gallerypage.html')


def loginpage(request):
    if request.method == 'POST':   
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username = username ,password =password)
        if user is not None:
            login(request,user)
            return redirect(HomePage)
        else:
            return HttpResponse("Invalid Details")
    else:
        return render(request,'loginpage.html')

def logoutpage(request):
    logout(request)
    return redirect(loginpage)

def registerpage(request):
    if request.method == "GET":
        form = RegistrationForm()
        return render(request,'registerpage.html',{'form':form})
    else:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save(commit=False)
            user.set_password(user.password)
            form.save()
            return redirect(loginpage)
        else:
            return HttpResponse("Invalid Form")

    
