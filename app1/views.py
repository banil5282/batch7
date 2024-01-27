import json


from django.shortcuts import render
from django.http import HttpResponse
from django.views.generic import View
from django.views.decorators.csrf import csrf_exempt
from .models import Persons
from django.shortcuts import redirect

# Create your views here.

def home(request):
    return render(request, "home.html")


def add(request):
	addtion = 20 + 20
	return HttpResponse(f"The sum is {addtion}")

def mul(request):
	result = 20 * 20
	return HttpResponse(f"The multiplication is {result}")


def div(request):
	result = 200 // 20
	return HttpResponse(f"The Division is {result}")

# @csrf_exempt
class Calculations(View):
	def get(self, request):
		return HttpResponse("Hello DJango!!!!!!!!!!!!")

	def post(self, request):
		return HttpResponse("Hello Python!!!!!!!!!!!!")

	def put(self, request):
		return HttpResponse("Hello Java!!!!!!!!!!!!")

	def delete(self, request):
		return HttpResponse("Hello C++!!!!!!!!!!!!")

class PersonDetails(View):
    def get(self, request):
        records = Persons.objects.all()
        if records:
            # return HttpResponse(records.values())
            return render(request, 'persons.html', {'persons': records})
        else:
            return HttpResponse("no records found")

    def post(self, request):
    	# breakpoint()
    	try:
    		person_id = request.POST['PersonID']
    		first_name = request.POST['FirstName']
    		last_name = request.POST['LastName']
    		address = request.POST['Address']
    		city = request.POST['City']
    	except:
    		body = json.loads(request.body)
	    	person_id = body.get('PersonID')
	    	first_name = body.get('FirstName')
	    	last_name = body.get('LastName')
	    	address = body.get('Address')
	    	city = body.get('City')

    	Persons.objects.create(
        	PersonID=person_id,
        	LastName=last_name,
        	FirstName=first_name,
        	Address=address,
        	City=city)
    	return HttpResponse(f"{first_name} record created succesfully")


def create_person(request):
	return render(request, "create_person.html")


def delete_person(request):
	# breakpoint()
	# body = json.loads(request.body)
	person_id = request.POST['id']
	delete_user = Persons.objects.filter(PersonID=person_id).delete()
	if delete_user:
		return redirect('/persons/')