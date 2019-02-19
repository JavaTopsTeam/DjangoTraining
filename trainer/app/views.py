from django.shortcuts import render
from .models import *
from .utils import *
# Create your views here.


def indexPage(request):
    return render(request,'app/details.html')

def addtrainerPage(request):
    return render(request,'app/addtrainer.html')



def index(request):
    all_info= info.objects.all()
    context={'all_info': all_info}
    return render(request,'app/details.html',context)



def addtrainer(request):
    firstname = request.POST['firstname']
    lastname = request.POST['lastname']
    email = request.POST['email']
    description = request.POST['description']
    date = request.POST['date']

    user = info.objects.filter(email = email)
    if user:
        message = 'This email already exists'
        return render(request,'app/addtrainer.html',{'message':message})
    else:
        newtrainer = info.objects.create(firstname=firstname,lastname=lastname,description=description,date=date,email=email)
        mail_subject = "New Trainer Hire"
        sendmail(mail_subject,'mail_template',email,{'name':firstname})
        return render(request,'app/success.html',{'newtrainer':newtrainer})

def store(request):
    obj = info()
    obj.id=request.GET['id']
    obj.firstname = request.GET['firstname']
    obj.lastname = request.GET['lastname']
    obj.description = request.GET['description']
    obj.date = request.GET['date']
    obj.email = request.GET['email']
    obj.save()
    all_info= info.objects.all()
    return render(request, 'app/index.html', {'all_info': all_info})

def insert(request):
    reco= info.objects.last()
    record = reco.id + 1
    return render(request, 'app/addtrainer.html',{'record':record})


def update(request):
    if 'update' in request.POST:
        obj_info = info.objects.get(id=request.GET['id'])
        mail_subject = "Update Profile"
        sendmail(mail_subject,'update_mail_template',email,{'name':firstname})
        return render(request, 'app/update.html',{'obj_info': obj_info})

    elif 'delete' in request.POST:
        delete_rec = info.objects.filter(id=request.GET['id'])
        delete_rec.delete()
        all_info = info.objects.all()
        mail_subject = "Update Profile"
        sendmail(mail_subject,'delete_mail_template',email,{'name':firstname})
        return render(request, 'app/index.html', {'all_info': all_info})
