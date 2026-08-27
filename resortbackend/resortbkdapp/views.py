from django.shortcuts import render,redirect,HttpResponse
#IMPORT FOR DATABASE USER REGISTRATION
from django.contrib.auth.models import User,auth
from django.contrib import messages
from django.contrib.auth import authenticate,login,logout
from django.contrib.auth.decorators import login_required
#IMPORTING FORMS KBV
from django import forms
from django.contrib.admin.widgets import AdminDateWidget,AdminSplitDateTime,AdminTimeWidget
#IMPORTING FOR SUITE KBV
from .models import addsuite
from .models import addtable
from .models import addvenue
from django.core.mail import message
from django.contrib import messages
from .models import Contact
# below import is done for sending emails
from django.conf import settings
from django.core.mail import send_mail
from django.core import mail
from django.core.mail.message import EmailMessage


# Create your views here.
@login_required(login_url='login')
def home(request):
    return render(request,'home.html')

def conv(request):
    return render(request,'conv.html')

def gallery(request):
    return render(request,'gallery.html')

def food(request):
    return render(request, 'food.html')

def expeditions(request):
    return render(request, 'expeditions.html')

def lq(request):
    return render(request, 'lq.html')

def submit(request):
    return render(request, 'submit.html')
#dropdown
def venue(request):
    return render(request, 'venue.html')

def payment(request):
    return render(request, 'payment.html')

def bs(request):
    return render(request, 'bs.html')



def SignupPage(request):
    if request.method=='POST':
        uname=request.POST.get('username')
        email=request.POST.get('email')
        pass1=request.POST.get('password1')
        pass2=request.POST.get('password2')

        if pass1!=pass2:
            return HttpResponse("Your password and confirm password are not Same!!")
        else:

            my_user=User.objects.create_user(uname,email,pass1)
            my_user.save()
            return redirect('login')
        
    return render (request,'signup.html')



def LoginPage(request):
    if request.method=='POST':
        username=request.POST.get('username')
        pass1=request.POST.get('pass')
        user=authenticate(request,username=username,password=pass1)
        if user is not None:
            login(request,user)
            return redirect('home')
        else:
            return HttpResponse ("Username or Password is incorrect!!!")

    return render (request,'login.html')



def LogoutPage(request):
    logout(request)
    return redirect('login')



def roombooking(request):
    if request.method=='POST':
        name=request.POST['name']
        email=request.POST['email']
        phone=request.POST['phone']
        
        checkindate=request.POST['checkindate']
        checkintime=request.POST['checkintime']
        checkoutdate=request.POST['checkoutdate']
        checkouttime=request.POST['checkouttime']
        roomtype=request.POST['roomtype']
    
        new_book=addsuite(name=name,email=email,phone=phone,checkindate=checkindate,checkintime=checkintime,checkoutdate=checkoutdate,checkouttime=checkouttime,roomtype=roomtype,)
        new_book.save()
    return render(request, 'roombooking.html')

def success(request):
    return render(request, 'bs.html')



def reserve(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        #venue=request.POST['venue']
        nooftables=request.POST['nooftables']
        date=request.POST['date']
        time=request.POST['time']
        message=request.POST['message']
        new_reserve=addtable(name=name,contact=contact,email=email,nooftables=nooftables,date=date,time=time,message=message)
        new_reserve.save()
    return render(request, 'reserve.html')



def venue(request):
    if request.method=='POST':
        name=request.POST['name']
        contact=request.POST['contact']
        email=request.POST['email']
        #venue=request.POST['venue']
        checkindate=request.POST['checkindate']
        checkoutdate=request.POST['checkoutdate']
        new_venue=addvenue(name=name,contact=contact,email=email,checkindate=checkindate,checkoutdate=checkoutdate)
        new_venue.save()
    return render(request,'venue.html')



























def contact(request):
    if request.method=="POST":
        fname=request.POST.get("name")
        femail=request.POST.get("email")
        phone=request.POST.get("phone")
        desc=request.POST.get("desc")
        query=Contact(name=fname,email=femail,phoneNumber=phone,description=desc)
        query.save()
        # emails sending starts from here
        from_email=settings.EMAIL_HOST_USER
        connection=mail.get_connection()
        connection.open()
        email_message=mail.EmailMessage(f'Email from {fname}',f'UserEmail : {femail}\nUserPhoneNumber : {phone}\n\n\n QUERY : {desc}',from_email,['aneesurrehman423@gmail.com','aneesrehman95567@gmail.com'],connection=connection)
        email_client=mail.EmailMessage('Arkprocoder Response','Thanks For Reaching us\n\narkprocoder.tech\n9986786453\nanees@arkprocoder.tech',from_email,[femail],connection=connection)

        connection.send_messages([email_message,email_client])
        connection.close()
        messages.info(request,"Thanks For Reaching Us! We will get back you soon....")
        return redirect('/contact')
    return render(request,'contact.html')
