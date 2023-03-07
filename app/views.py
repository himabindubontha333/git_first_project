from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.
def Hima(request):
    return HttpResponse("<h1><Marquee>Take it is easy policy</Marquee></h1>")