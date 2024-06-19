from django.shortcuts import render
# import httpresponse to create httpresponse
from django.http import HttpResponse

# Create your views here.
def index(request):
    return HttpResponse('<h1>Hey, Welcome To Homepage.</h1>')
