from django.shortcuts import render, HttpResponse

# Create your views here.
def home(request):
    return render(request, 'home.html')

def about(request):
    return render(request, 'about.html')

def faqs(request):
    return render(request, 'faqs.html')

def contact(request):
    return render(request, 'contact.html')

def registration(request):
    return render(request, 'registration.html')

def choice(request):
    return render(request, 'choice.html')

def seat(request):
    return render(request, 'seat.html')

def apply(request):
    return render(request, 'apply.html')

def apply2(request):
    return render(request, 'apply2.html')