from django.shortcuts import render
from .models import Employee 
import datetime


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
    if request.method == 'POST':
        first_name=request.POST['first_name']
        last_name=request.POST['last_name']
        dept=request.POST['dept']
        salary=request.POST['salary']
        bonus=request.POST['bonus']
        role=request.POST['role']
        phone=request.POST['phone']
        hire_date=datetime.datetime.now()
        ins=Employee(first_name=first_name,last_name=last_name,dept=dept,salary=salary,bonus=bonus,role=role,phone=phone,hire_date=hire_date)
        ins.save()
        return render(request,'add.html',context = {'success' : True})
    return render(request,'add.html')
        
    # elif request.method=='GET':
    #     return render(request,'add.html')

def remove (request):
    return render(request,'remove.html')

def filter (request):
    return render(request,'filter.html')
