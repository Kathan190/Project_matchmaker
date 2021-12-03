from django.shortcuts import render
from django.http import HttpResponse, request
from Home.models import Contact
from Home.models import Course

# Create your views here.


def home(request):
    return render(request, 'home/home.html')

def about(request):
    return render(request, 'home/about.html')

def index(request):
    return render(request, 'home/index.html')

def contact(request):
    if request.method == "POST":
        email = request.POST.get('email')
        fname = request.POST.get('fname')
        cnumber = request.POST.get('cnumber')
        contact = Contact(email=email, fname=fname, cnumber=cnumber)
        contact.save()
        return render(request, 'Home/contact.html')
    return render(request, 'Home/contact.html')
    
def main(request):
    context = {
        'courses':Course.objects.all()
    }
    return render(request, 'home/main.html', context)