from django.shortcuts import render
from django.http import HttpResponse
def welcome(Request):
	print("-+"*20)
	print("Request received at welcome")
	print("-+"*20)



def abc(Request):
	print("-+"*20)
	print("Request received at abc")
	print("-+"*20)
	return render(Request,'welcome.html')
	#return HttpResponse('Hello')
# Create your views here.
