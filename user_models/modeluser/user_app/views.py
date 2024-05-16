from django.shortcuts import render
from . forms import userForm
# from django.contrib.auth.forms import UserCreationForm  
# Create your views here.
def index(request):
    userF=userForm()
    return render(request,"index.html",{'userF':userF})
# def index(request):
    
#     userF=UserCreationForm()
#     return render(request,"index.html",{'userF':userF})