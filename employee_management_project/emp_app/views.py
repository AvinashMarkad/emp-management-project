from django.shortcuts import render

# Create your views here.
def index (request):
    return render(request,'index.html')

def view (request):
    return render(request,'view.html')

def add (request):
    return render(request,'add.html')

def remove (request):
    return render(request,'remove.html')

def filter (request):
    return render(request,'filter.html')
