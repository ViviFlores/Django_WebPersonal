from django.shortcuts import render

# Create your views here.


def home(request):  # petición
    return render(request, "core/home.html")


def about(request):
    return render(request, "core/about.html")


def contact(request):
    return render(request, "core/contact.html")
