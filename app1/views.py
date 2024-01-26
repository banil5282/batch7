from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def add(request):
	addtion = 20 + 20
	return HttpResponse(f"The sum is {addtion}")

def mul(request):
	result = 20 * 20
	return HttpResponse(f"The multiplication is {result}")


def div(request):
	result = 200 // 20
	return HttpResponse(f"The Division is {result}")