from django.shortcuts import render, redirect
from .models import Userinfo
from .forms import UserinfoForm
# Create your views here.

def Register(request):
    if request.method == 'POST':
        form = UserinfoForm(request.POST)
        if form.is_valid():
            form.save()
            
    else:
        form = UserinfoForm()
    return render(request,'register.html',{'form':form})

def read(request):
    read = Userinfo.objects.all(id)
    return render(request, 'read.html',{'read':read})