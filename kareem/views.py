from django.shortcuts import render
from django.http import HttpResponse
# Create your views here.
def Home(reqeust):
   #return HttpResponse('<h1> Hello </h1>')
   return render(reqeust,'kareem/home.html')