from django.shortcuts import render , redirect
from django.http import HttpResponse
from .models import UserContactDetails
from .forms import UserContactRegistration
from django.core.mail import send_mail
from .task import * 


def home(request):
  return render(request,'base.html')


def aboutus(request):
  return render(request,'aboutus.html')

# User Contact Details 

def create_view(request):
  if request.method == 'POST':
    form = UserContactRegistration(request.POST)
    # Email Sending On User And Admin Mail Inbox
    
    recepient = str(form['user_email'].value())
    subject = 'User Inform Create'
    message = 'You have Succesfully Created Your Account' 
    send_mail_user_task.delay(recepient,subject,message)
    
    # End Code Email Sending User And Admin Inbox
    
    if form.is_valid():
      form.save()
      return redirect("home")
  else:
    form = UserContactRegistration()
  return render(request,'createview.html',{'form':form})

# End Code User Contact Details 
