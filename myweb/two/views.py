from django.http import HttpResponse
from urllib import request
from django.shortcuts import render
# Create your views here.
def dashboard(response):
    return HttpResponse('show dashboard!!!')

def search(response):
    return HttpResponse('search and export!!!')