from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def hello(request):
    return HttpResponse('<h3>Welcome to Heroku Successfully Deployement By Shivam Kumar Sinha</h3>')
