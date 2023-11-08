from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def seenu(request):
    return HttpResponse('<h1><marquee>ramesh:hi seenu how r u what r u doing</h1></marquee>')
def ramesh(request):
    return HttpResponse('<h1><marquee>seenu:iam fine how r u ramesh</h1></marquee>')