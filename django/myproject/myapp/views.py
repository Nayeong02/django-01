from django.http import HttpResponse
from django.shortcuts import render, HttpResponse
from django.template import loader 

# Create your views here.

def index(request) :
    template = loader.get_template('home.html')
    return HttpResponse(template.render())
    #return HttpResponse("<h1>안녕하세요 윤나영입니다</h1>")

def shop(request) :
    template = loader.get_template('shop.html')
    return HttpResponse(template.render())

def create(request) :
    return HttpResponse("<h1>안녕하세요 create입니다</h1>")

def read(request, id) :
    return HttpResponse("<h1>안녕하세요 read입니다</h1>" + id)
