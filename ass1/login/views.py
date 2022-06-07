from django.shortcuts import render,HttpResponse
from django.db import models
import os
import random
from requests import request
from twilio.rest import Client
from django.contrib import messages

otp=None
otp=random.randint(1000,9999)
def load(request):
    return render(request,"login.html")

def login(request):
    
    if request.method=="POST":
        phone_number=request.POST['phone']
        print(phone_number+" "+str(otp))
        account_sid = 'ACd43c65cc36477c6c2f0e29fbc03667ef'
        auth_token = '48ddf73ebfc19f898d973af7836c2c7f'
        client = Client(account_sid, auth_token)
        op_txt="Your OTP is: "+str(otp)
        number_p="+91"+str(phone_number)

        message = client.messages.create(
                              body= op_txt,
                              from_='+17242623038',
                              to=number_p
                          )

        print(message.sid)
        #print("hii"+str(otp))
             
    return render(request,'home.html')

def home(request):
    print("OTP:"+str(otp))
    if request.method=="POST":
        otp1=request.POST['otp']
        print("OTP:"+str(otp1)+" "+str(otp))
        if(str(otp1)==str(otp)):
            return HttpResponse("Success")
    return HttpResponse("Unsuccessful")
