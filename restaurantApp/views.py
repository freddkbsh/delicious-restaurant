from django.shortcuts import render,redirect
from restaurantApp.credentials import MpesaAccessToken, LipanaMpesaPpassword
from restaurantApp.forms import Table1Form, ImageUploadForm
from restaurantApp.models import Table1, Contact2, ImageModel
from requests.auth import HTTPBasicAuth
from django.http import HttpResponse
import json

import requests


# Create your views here.
def index(request):
    return render(request, 'index.html')
def starter(request):
    return render(request,'starter-page.html')

def about(request):
    return render(request,'about.html')

def menu(request):
    return render(request,'menu.html')


def events(request):
    return render(request,'events.html')


def table(request):
    if request.method=='POST':
        mytable=Table1(
            name=request.POST['name'],
            email=request.POST['email'],
            phone=request.POST['phone'],
            date=request.POST['date'],
            time=request.POST['time'],
            people=request.POST['people'],
            message=request.POST['message'],


        )
        mytable.save()
        return redirect('/table')
    else:
        return render(request,'book-table.html')

def contact(request):
    if request.method=='POST':
        mycontact=Contact2(
            name=request.POST['name'],
            email=request.POST['email'],
            subject=request.POST['subject'],
            message=request.POST['message'],
        )
        mycontact.save()
        return redirect('/contact')
    else:
        return  render(request,'contact.html')

def gallery(request):
    return render(request,'gallery.html')

def specials(request):
    return render(request,'specials.html')

def chefs(request):
    return render(request,'chefs.html')

def display(request):
    alltable=Table1.objects.all()
    return  render(request,'display.html',{'table':alltable})

def delete(request,id):
    appoint=Table1.objects.get(id=id)
    appoint.delete()
    return redirect('/display')

def edit(request,id):
    mine=Table1.objects.get(id=id)
    return render(request,'edit.html',{'table':mine})

def update(request,id):
    info=Table1.objects.get(id=id)
    form=Table1Form(request.POST, instance=info)
    if form.is_valid():
        form.save()
        return redirect('/display')
    else:
       return render(request,'edit.html')
def upload_image(request):
    if request.method == 'POST':
        form = ImageUploadForm(request.POST, request.FILES)
        if form.is_valid():
            form.save()
            return redirect('/showimage')
    else:
        form = ImageUploadForm()
    return render(request, 'upload_image.html', {'form': form})

def show_image(request):
    images = ImageModel.objects.all()
    return render(request, 'show_image.html', {'images': images})

def token(request):
    consumer_key = 'UsewVQAAGDBKCAboosOtxzufPu8BiYcpEfulelaKETDNrkoy'
    consumer_secret = 'a7hVRZvp0cmNFQF9JbibP34Bx5QwwVpG2ADZABtkrL8aHHfZdh6cC21rBLkGOw4x'
    api_URL = 'https://sandbox.safaricom.co.ke/oauth/v1/generate?grant_type=client_credentials'

    r = requests.get(api_URL, auth=HTTPBasicAuth(
        consumer_key, consumer_secret))
    mpesa_access_token = json.loads(r.text)
    validated_mpesa_access_token = mpesa_access_token["access_token"]

    return render(request, 'token.html', {"token":validated_mpesa_access_token})

def pay(request):
   return render(request, 'pay.html')



def stk(request):
    if request.method =="POST":
        phone = request.POST['phone']
        amount = request.POST['amount']
        access_token = MpesaAccessToken.validated_mpesa_access_token
        api_url = "https://sandbox.safaricom.co.ke/mpesa/stkpush/v1/processrequest"
        headers = {"Authorization": "Bearer %s" % access_token}
        request = {
            "BusinessShortCode": LipanaMpesaPpassword.Business_short_code,
            "Password": LipanaMpesaPpassword.decode_password,
            "Timestamp": LipanaMpesaPpassword.lipa_time,
            "TransactionType": "CustomerPayBillOnline",
            "Amount": amount,
            "PartyA": phone,
            "PartyB": LipanaMpesaPpassword.Business_short_code,
            "PhoneNumber": phone,
            "CallBackURL": "https://sandbox.safaricom.co.ke/mpesa/",
            "AccountReference": "eMobilis",
            "TransactionDesc": "Web Development Charges"
        }
        response = requests.post(api_url, json=request, headers=headers)
        return HttpResponse("Success")