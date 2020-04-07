from django.shortcuts import render,get_object_or_404
from django.http import HttpResponse
from .models import Patient

def home_page(request):
    #return HttpResponse("hellooooooooo")
    return render(request,'dental/home_page.html')

def login_page(request):
    return render (request,'dental/login.html')

def create_account(request):
    return HttpResponse("this is creating_account page :)")

def user_panel(request):
    number=request.POST['patient_id']
    try:
        patient=Patient.objects.get(pk=number)
    except Patient.DoesNotExist:
        return render(request,'dental/login.html', {'error_message':"wrong password"})

    else:
        Attribute_list=[]
        Attribute_list.append(patient.name)
        Attribute_list.append(patient.lastname)
        Attribute_list.append(patient.address)
        Attribute_list.append(patient.phone_number)
        return render(request,'dental/user_panel.html',{'patient':Attribute_list})


# Create your views here.
