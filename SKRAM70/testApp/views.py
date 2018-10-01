from django.shortcuts import render
from .models import Cars
from .models import Customers
from .models import Stores
from .models import Orders
from django.http import HttpResponse
from django.http import HttpResponseRedirect
from django import forms
from .functions.timeobjects import *
from .functions.search import *
from .functions.inputVerification import *
from django.contrib import messages
from .forms import *
from .functions.vehicleReturns import *
from django.core.mail import send_mail
from .functions.renderPdf import renderPDF

def index(request):
    storelist = Stores.objects.all()
    context = {'StoreList': storelist}
    return render(request, 'testApp/AlanaCustomerHomepage.html', context)

def detail(request, car_id):
    carInfo = Cars.objects.filter(id=car_id)
    context = {'CarInfo': carInfo}
    return render(request, 'testApp/showcaroriginal.html', context)

def contactUs(request):
    querySuccesfullySubmitted = False
    failedToSubmit = False
    if request.method == 'POST':
        form = CustomerQuery(request.POST)
        if form.is_valid():
            subject = "issue from: " + form.cleaned_data['your_name']
            sender = form.cleaned_data['email']
            message = form.cleaned_data['question']
            recipients = ['companyEmail@noreply.com']
            send_mail(subject, message, sender, recipients)
            querySuccesfullySubmitted = True
        else:
            failedToSubmit = True
    else:
        form = CustomerQuery()
    context = {'form': form, 'querySuccesfullySubmitted': querySuccesfullySubmitted, 'failedToSubmit': failedToSubmit}
    return render(request, 'testApp/MikeContactPage draft.html', context)

def accounts(request):
    if request.method == "POST":
        if (request.POST.get('firstname') and request.POST.get('middlename') and request.POST.get('lastname') and request.POST.get('tel') and request.POST.get('bday') and request.POST.get('email') and request.POST.get('Password')):

            post = Customers()
            f = forms.CharField()
            post.name = (f.clean(request.POST.get('firstname')) + ' ' + f.clean(request.POST.get('middlename')) + ' ' + f.clean(request.POST.get('lastname')))
            post.phone = f.clean( request.POST.get('tel'))
            # post.address = f.clean( request.POST.get('Address'))
            post.dob = f.clean( request.POST.get('bday'))
            post.email = f.clean(request.POST.get('email'))
            post.password = f.clean(request.POST.get('Password'))
            post.save()
            return render(request, 'testApp/ShaleenCreateYourAccountPage.html')
        else:
            return render(request,'testApp/ShaleenCreateYourAccountPage.html')
    else:
        return render(request,'testApp/ShaleenCreateYourAccountPage.html')


def staffPortal(request):
    return render(request, 'testApp/MikeStaffHomePage.html')

def returnPage(request):
    zippedResults = VehicleReturns.vehicleToBeReturned(request)
    storelist = Stores.objects.all()
    context = {'zippedResults': zippedResults, 'StoreList': storelist, 'Period': zippedResults}
    if request.method == 'GET' and 'pdf' in request.GET:
        return renderPDF('testApp/pdf.html', context)
    return render(request, 'testApp/MikeCarReturnPage.html', context)

def search(request):
    if request.method == 'GET':
        resultantCars = carSets.searchData(request)
    elif request.method == 'POST':
        resultantCars = carSets.reccomendCars(request)
    else:
        resultantCars = Cars.objects.all()

    storelist = Stores.objects.all()
    context = {'resultantCars': resultantCars, 'StoreList': storelist}
    return render(request, 'testApp/ShaleenSearchresults.html', context)
