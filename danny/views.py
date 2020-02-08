from django.contrib import messages
from services.models import services
from testmonials.models import testimonies
from django.shortcuts import render,redirect
from django.contrib.auth.models import User, auth
from django.contrib.auth.decorators import login_required
from django.core.mail import BadHeaderError, send_mail
from django.http import HttpResponse, HttpResponseRedirect
from blogging.models import Post


# Create your views here.
def index(request):
    return render(request,'index.html',{})

def contacts(request):
    return render(request,'contacts.html',{})

    

def mytestimonials(request):
    testmony=testimonies.objects.all()
    return render(request,'testimonials.html',{'testmony': testmony})

def myservices(request):
    service = services.objects.all()
    return render(request,'services.html',{'service': service})

def blog(request):
    posts = Post.objects.all()
    return render(request,'blog/post_list.html',{'posts':posts})









def register(request):
    if request.method == 'POST':
        first_name= request.POST['first_name']
        last_name= request.POST['last_name']
        username= request.POST['username']
        password1= request.POST['password1']
        password2= request.POST['password2']
        email= request.POST['email']


        if password1==password2:
            if User.objects.filter(username=username).exists():
                messages.info(request,'Username Taken')
                return redirect('register')
            elif User.objects.filter(email=email).exists():
                messages.info(request,'Email Taken')
                return redirect('register')
            else:
                user= User.objects.create_user(username=username,password=password1,email=email, first_name=first_name, last_name=last_name)
                user.save();
                print('User created')
                return redirect('login')

        else:
            messages.info(request,'password not matching') 
            return redirect('register')       
        return redirect('/')


    else:
        return render(request,'register.html')




def login(request):
    if request.method=='POST':
        username= request.POST['username']
        password= request.POST['password']

        User = auth.authenticate(username=username, password=password)

        if User is not None:
            auth.login(request,User)
            return redirect('index')
        else:
            messages.info(request,'invalid credentials')
            return redirect('login')

    else:
        return render(request,'login.html')


