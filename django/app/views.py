from django.shortcuts import render
from .models import newuser
from .forms import UserRegister
# Create your views here.

def RegistrationPage(request):
    return render(request,'app/register.html')

def UserFormRegister(request):
    form = UserRegister()
    return render(request,'app/register2.html',{'form':form})

def user_register(request):
    first_name = request.POST['first_name']
    last_name = request.POST['last_name']
    mobile = request.POST['mobile']
    profile_pic = request.FILES['profile_pic']

    new_user = newuser.objects.create(first_name= first_name,last_name=last_name,mobile=mobile,profile_pic=profile_pic)
    return render(request,"app/user-profile.html",{'user_data':new_user})



def user_form_register(request):
    if request.method == 'POST':

        form = UserRegister(request.POST,request.FILES)

        if form.is_valid():
            post = form.save(commit=False)
            post.first_name = form.cleaned_data['first_name']
            post.last_name = form.cleaned_data['last_name']
            post.mobile = form.cleaned_data['mobile']
            post.profile_pic = form.cleaned_data['profile_pic']
            post.save()
            return render(request,'app/user-info.html',{'user':post})
    else:
        form = UserRegister(request.POST)
        return render(request,'app/user-info.html',{'form':form})
