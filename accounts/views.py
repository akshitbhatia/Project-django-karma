from django.conf import settings
from django.core.mail import send_mail
from django.shortcuts import render, redirect
from django.contrib.auth.models import User
from django.contrib import auth



# Create your views here.



def verify(request):
    if request.method == 'POST':
        try:
            if request.POST['verify_code'] == '13bme1045':
                return redirect('home')
            else:
                return render(request, 'accounts/verify.html', {'error':'*Verification code is not correct, Try Again!'})
        except:
            return render(request, 'accounts/verify.html',{'error':'*Verification code is not correct'})
    else:
        return render(request, 'accounts/register.html')




def register(request):
    if request.method == 'POST':
        if request.POST['password1'] ==  request.POST['password2']:
            try:
                user = User.objects.get(username=request.POST['username'])
                return render(request, 'accounts/register.html',{'error':'*Email Already Been Taken, Try with another Email.'})

            except User.DoesNotExist:
                subject = 'Verification Process'
                message = "Hi\nThank you for registering for karmaa lab\n Here is your Verification  code: 13bme1045\n\n\nBest Regards\nKarmaa Labs"
                from_email = settings.EMAIL_HOST_USER
                to_list = [request.POST['username'],settings.EMAIL_HOST_USER]
                send_mail(subject, message, from_email, to_list, fail_silently=True)

                user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
                auth.login(request, user)
                return render(request, 'accounts/verify.html')
                # return redirect('verify')


        else:
            return render(request,'accounts/register.html',{'error':'*Password Must Match.'})
    else:
        return render(request,'accounts/register.html')






def login(request):
    if request.method=="POST":
       user= auth.authenticate(username=request.POST['username'],password=request.POST['password'])
       if user is not None:
           auth.login(request,user)
           return redirect('home')
       else:
           return render(request, 'accounts/login.html',{'error':'*Username or Password Incorrect'})
    else:
        return render(request,'accounts/login.html')





def logout(request):
    if request.method=="POST":
        auth.logout(request)
        return redirect('home')
        # return render(request, 'accounts/login.html')









# def verify(request):
#     if request.method == 'POST':
#         try:
#             if request.POST['verify_code'] == '2019':
#                 return redirect('home')
#             else:
#                 return render(request, 'accounts/verify.html', {'error':'*Verification code is not correct, Try Again!'})
#         except:
#             print("Email not sent !")
#     else:
#         return render(request, 'accounts/register.html')
#
#
#
#
# def register(request):
#     if request.method == 'POST':
#         if request.POST['password1'] ==  request.POST['password2']:
#             try:
#                 user = User.objects.get(username=request.POST['username'])
#                 return render(request, 'accounts/register.html',{'error':'*Email Already Been Taken, Try with another Email.'})
#
#             except User.DoesNotExist:
#                 subject = 'Verification Process'
#                 message = "Hi\nThank you for registering for karmaa lab\n Here is your Verification  code: 059108.\n\n\nBest Regards\nKarmaa Labs"
#                 from_email = settings.EMAIL_HOST_USER
#                 to_list = [request.POST['username'],settings.EMAIL_HOST_USER]
#                 send_mail(subject, message, from_email, to_list, fail_silently=True)
#
#                 user=User.objects.create_user(request.POST['username'], password=request.POST['password1'])
#                 auth.login(request, user)
#                 return render(request, 'accounts/verify.html')
#                 # return redirect('verify')
#
#
#         else:
#             return render(request,'accounts/register.html',{'error':'*Password Must Match.'})
#     else:
#         return render(request,'accounts/register.html')
#
