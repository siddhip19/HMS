from django.shortcuts import render
from django.http import HttpResponse
from .models import Contact

# Create your views here.
def index(request):
    return HttpResponse("home page")

def contact(request):
    if request.method == 'POST':
        name = request.POST.get('name', '')
        email = request.POST.get('email', '')
        phone = request.POST.get('phone', '')
        message = request.POST.get('message', '')
        category = request.POST.get('category','')
        contact = Contact(name = name, email = email, category = category, message = message, phone = phone)
        contact.save()
    return render(request,'health/contact.html')

def login(request):
    return render(request, 'health/login.html')

def register(request):
    return render(request, 'health/register.html')

def otp(request):
    return render(request, 'health/otp.html')