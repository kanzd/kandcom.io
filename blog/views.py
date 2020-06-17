from django.shortcuts import render
from django.http import *
# Create your views here.
def index(req):
    return render(req,'blog/blog.html')
def aboutus(req):
    return HttpResponse("<a href='contactus'>yo</a>")
def contactus(req):
    return HttpResponse("ok")