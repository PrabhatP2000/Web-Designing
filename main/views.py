from django.http.response import HttpResponse
from django.shortcuts import render, HttpResponse,redirect
from django.contrib.auth.decorators import login_required
from django.core.mail import send_mail
from webdev import settings
from django.contrib.auth import logout,login,authenticate
from django.contrib import messages
from .models import ResultProfile
from .models import AdmissionEnquiry

# Create your views here.

def index(request):
    return render(request, 'index.html')


def contact(request):
    return render(request,'contact.html')

def admission_form(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        subject = request.POST['subject']
        message = request.POST['message']
        admission_enquiry =AdmissionEnquiry(NAME=name,EMAIL=email,SUBJECT=subject,MESSAGE=message)
        admission_enquiry.save()
        messages.success(request, " Form Successfully Sent")
        return render(request, 'contact.html')
        
    else:
        return render(request, '404.html')
        


def gallery(request):
    return render(request,'gallery.html')



def te_result(request):
    return render(request,'te_result.html')

def comp_department(request):
    return render(request,'comp_dept.html')


def result(request):
    if request.user.is_authenticated:
        username=request.user.username
        result_profile = ResultProfile.objects.filter(ERP=username)
        result_data={"result_profile":result_profile}
        return render(request,'result.html',result_data)
    else:
        return render(request,'404.html')
    


def user_login(request):
    if request.method == 'POST':
        erp = request.POST['erp']
        login_password = request.POST['password']

        user = authenticate(username=erp,
                            password=login_password)
        if user is not None:
            login(request, user)
            messages.success(request, " Successfully Logged In")
            return render(request, 'index.html')
        else:
            messages.error(request, " Invalid Credentials")
            return render(request, 'index.html')
    return render(request, '404.html')
    

def user_logout(request):
   logout(request)
   messages.success(request, "Successfully Logged Out")
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
