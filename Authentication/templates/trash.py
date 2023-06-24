from django.shortcuts import render, redirect
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout
from .forms import UserformAPI, UserRegisterAPI      #dev'ing of models
from django.http import HttpResponse
from django.contrib.auth.models import User

# Create your views here.
@login_required
def index(request):
    return render(request, 'base.html', {})
    
def signin(request):
    form = UserformAPI()
    if request.method == 'POST':
        form = UserformAPI(request.Post)
        if form.is_valid():
            # email = request.POST['email']
            # password = request.POST['password']
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password')
            if user:
                user = authenticate(request, email = email, password = password)
                login(request, user)
                return redirect('/')
            elif user == None:
                return HttpResponse("Invalid credentials.")
        else:
            form = UserformAPI()
            return render(request, 'login.html', {'form': form})
        

def signout(request):
    logout(request)
    return redirect('/')
    
        

def signup(request):
    if request.method == 'POST':
        firstname = request.POST['first_name']
        lastname = request.POST['last_name']
        username = request.POST['username']
        password = request.POST['password']
        email = request.POST['email']
        newuser = User.objects.create_user( first_name = firstname, last_name = lastname, username = username, email= email, password = password)
        try:
            newuser.save()
        except:
            return render('Something went wrong')
    else:
        form = UserRegisterAPI()
        return render(request, 'signup.html', {'form': form})
