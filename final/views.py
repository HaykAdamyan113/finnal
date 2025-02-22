from django.http import HttpResponse
from django.shortcuts import render

def homepage(request):
    #return HttpResponse("YOU CAN SK MY DK IF U DONT LIKE MY ST")
    return render(request,'home.html')

def about(request):
    #return HttpResponse("and this is about page deeer")
    return render(request,'about.html')