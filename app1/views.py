from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request):
	addtion = 20 + 20
	return HttpResponse(f"The sum is {addtion}")

