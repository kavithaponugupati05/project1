from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse
def hai(request):
    return HttpResponse('<h1>this is our first fbv</h1>')
def hello(request):
    return HttpResponse('<h1><marquee>this is our second fbv</marquee></h1>')
    
