from django.shortcuts import render

from django.http import HttpResponse

# Create your views here.
def index(request):
	#return HttpResponse("Hello, world")
	return render(request,"hello/index.html")
def say_hello(request):
	return HttpResponse("Hello, Rishi")

def great(request,name):
	#return HttpResponse(f"Hello, {name.capitalize()}")
	return render(request,"hello/great.html",{

		"name":name.capitalize()

		})
