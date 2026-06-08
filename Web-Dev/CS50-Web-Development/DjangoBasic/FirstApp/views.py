from django.http import HttpResponse
from django.shortcuts import render

# Create your views here.
def index(request):  # HTTP request
    return render(request, "hello/index.html")

def jack(request):
    return HttpResponse("Hello, Jack!")

def leo(request):
    return HttpResponse("Hello Leo!")

def greet(request, name):
    # return HttpResponse(f"Hello, {name.capitalize()}!")
    return render(request, "hello/greet.html", {
        "name": name.capitalize()
    })
