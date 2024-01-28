from django.shortcuts import render
from .models import Employee

# Create your views here.
def index (request):
    return render(request,'index.html')

def view (request):
    emps = Employee.objects.all()
    context={
        'emps':emps
    }
    
    return render(request,'view.html',context)

def add (request):
    return render(request,'add.html')

def remove (request):
    return render(request,'remove.html')

def filter (request):
    return render(request,'filter.html')
