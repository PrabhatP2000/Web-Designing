from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from webdev import settings
from django.contrib.auth import logout
from .models import ResultProfile

# Create your views here.

def index(request):
    return render(request, 'index.html')

def te_result(request):
    return render(request,'te_result.html')

@login_required
def result(request):
    result_profile = ResultProfile.objects.all()
    result_data={"result_profile":result_profile}
    return render(request,'result.html',result_data)

def login_signup(request):
    return render(request,'login_signup.html')

def user_logout(request):
   logout(request)
   return render(request, 'index.html')

    
# def email(request):
#     digits = [i for i in range(0, 10)]
#     random_str = ""
#     for i in range(6):
#         index = math.floor(random.random() * 10)
#         random_str += str(digits[index])
#     print(random_str,type(random_str))
#     subject = 'AVCOE Remastered OTP Verification'
#     message = 'Thank You for Registering on AVCOE Remastered.\nYour OTP is ' + random_str + '\nUse this to Verify Your Account'
#     email_from = settings.EMAIL_HOST_USER
#     recipient_list = ['mukundwagh2000@gmail.com',]
#     send_mail( subject, message, email_from, recipient_list )
#     return redirect('index')
