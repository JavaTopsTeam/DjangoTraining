from django.shortcuts import render
from .models import *
from random import randint
from .util import *
# Create your views here.


def RegistrationPage(request):
    return render(request,"doctorfinder/register.html")


def LoginPage(request):
    return render(request,"doctorfinder/login.html")


def ForgotPage(request):
    return render(request,"doctorfinder/forgot.html")




def registeruser(request):
    try:
        if request.POST['role'] == 'doctor':
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            speciality = request.POST['speciality']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            gender = request.POST['gender']
            city = request.POST['city']
            mobile = request.POST['phone']
            dateofbirth = request.POST['birthdate']

            user = User.objects.filter(email = email)
            if user:
                message = 'This email is already registered'
                return render(request,'doctorfinder/register.html',{'message':message})
            else :
                if password == confirmpassword:
                    otp = randint(100000,9999999)
                    print(otp)
                    newuser = User.objects.create(email = email,password = password,role = role,otp=otp)
                    newdoctor = Doctor.objects.create(user_id = newuser,firstname = firstname,lastname = lastname, speciality = speciality,gender = gender,mobile = mobile, birthdate = dateofbirth,city = city)
                    email_subject = "Your Otp number for verify your account"
                    sendmail(email_subject,'mail_template',email,{'name':firstname,'otp':otp,'link':'http://localhost:8000/doctorfinder/user_verify/'})
                    return render(request,'doctorfinder/RegisterSuccessful.html')
                else:
                    message = 'Password does not match with your confirm password'
                    return render(request,'doctorfinder/register.html',{'message':message})

        else:
            role = request.POST['role']
            firstname = request.POST['firstname']
            lastname = request.POST['lastname']
            email = request.POST['email']
            password = request.POST['password']
            confirmpassword = request.POST['confirmpassword']
            gender = request.POST['gender']
            city = request.POST['city']
            mobile = request.POST['phone']

            user = User.objects.filter(email = email)
            if user:
                message = 'This email is already registered'
                return render(request,'doctorfinder/register.html',{'message':message})
            else :
                if password == confirmpassword:
                    otp = randint(100000,9999999)
                    print(otp)
                    newuser = User.objects.create(email = email,password = password,role = role,otp=otp)
                    newpatient = Patient.objects.create(user_id = newuser,firstname = firstname,lastname = lastname, gender = gender,mobile = mobile,city = city)
                    email_subject = "Your Otp number for verify your account"
                    sendmail(email_subject,'mail_template',email,{'name':firstname,'otp':otp,'link':'http://localhost:8000/doctorfinder/user_verify/'})
                    return render(request,'doctorfinder/login.html')
                else:
                    message = 'Password does not match with your confirm password'
                    return render(request,'doctorfinder/register.html',{'message':message})
    except User.DoesNotExist:
        message = 'This email is already registered'
        return render(request,'doctorfinder/register.html',{'message':message})



def loginuser(request):
    if request.POST['role'] == 'doctor':
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email = email)
        if user[0]:
            if user[0].password == password and user[0].role == 'doctor':
                doctor = Doctor.objects.filter(user_id = user[0])
                request.session['email'] = user[0].email
                request.session['firstname'] = doctor[0].firstname
                return render(request,'doctorfinder/homepage_doctor.html')
            else:
                print("doctorhello1")
                message = 'Your email else password is worng please check it'
                return render(request,'doctorfinder/login.html',{'message':message})
        else:
            message = "User is not exist"
            return render(request,'doctorfinder/login.html',{'message':message})
    else:
        email = request.POST['email']
        password = request.POST['password']
        user = User.objects.filter(email = email)
        print(user)
        if user[0]:
            if user[0].password == password and user[0].role == 'patient':
                patient = Patient.objects.filter(user_id = user[0])
                request.session['email'] = user[0].email
                request.session['firstname'] = patient[0].firstname
                return render(request,"doctorfinder/homepage_patient.html")
            else:
                message = "Your password is incorrect or user doesn't exist"
                return render(request,"doctorfinder/login.html",{'message':message})
        else:
            message = "user doesn't exist"
            return render(request,"doctorfinder/login.html",{'message':message})



def userforgot_email_verify(request):
    try:
        email = request.POST['email']
        user = User.objects.get(email = email)
        print(user)
        if user:
            otp = randint(100000,9999999)
            print(otp)
            user.otp = otp
            user.save()
            email_subject = " Your OTP for forgot password is :"
            sendmail(email_subject,'mail_template',email,{'otp':otp,'link':'http://localhost:8000/doctorfinder/user_verify/'})
            return render(request,'doctorfinder/ResetPassword.html')
        else:
            print("hello1")
            message = 'Your email does not exist'
            return render(request,'doctorfinder/forgot.html',{'message':message})
    except User.DoesNotExist:
        print("hello2")
        message = 'This email does not exists'
        return render(request,'doctorfinder/forgot.html',{'message':message})


def resetPassword(request):
    try:
        email = request.POST['email']
        otp = request.POST['otp']
        newpass = request.POST['newpassword']
        newconfirmpass = request.POST['newconfirmpassword']
        user = User.objects.get(email = email)
        print(user)
        print(type(otp))
        print(type(user.otp))
        print(newpass)
        print(newconfirmpass)
        if user:
            if user.otp == otp:
                if newpass == newconfirmpass:
                    user.password = newpass
                    user.save()
                    email_subject = "Your Password Updated Successfully "
                    sendmail(email_subject,'mail_template',email,'')
                    return render(request,'doctorfinder/login.html',{'email':email})
                else:
                    message = "Your password and confirm password doest not match"
                    return render(request,'doctorfinder/ResetPassword.html',{'message':message})
            else:
                message = "Your OTP doesnot match"
                return render(request,'doctorfinder/ResetPassword.html',{'message':message})
        else:
            message = "User does not exist"
            return render(request,'doctorfinder/forgot.html',{'message':message})
    except User.DoesNotExist:
        message = 'This email does not exists'
        return render(request,'doctorfinder/register.html',{'message':message})
