from django.shortcuts import render
from .models import Rooms,ContactForm

# Create your views here.
def index(request):

    rooms = Rooms.objects.all()
    return render(request,"index.html",{'rooms':rooms})

def Room(request):
    rooms = Rooms.objects.all()
    return render(request,"products.html",{'rooms':rooms})    

def aboutus(request):
    return render(request,"about.html")    
def contactus(request):

    return render(request,"contact.html") 

def contactform(request):
    name = request.POST["name"]
    email = request.POST["email"]
    subject = request.POST["subject"]
    message = request.POST["message"]

    contactform = ContactForm(name=name,email=email,subject=subject,message=message)
    contactform.save()
    return render(request,"contact.html") 
            