from django.shortcuts import render
from bt.models import Teacher
from . form import  teacherRegistration
from django.contrib.auth.forms import UserCreationForm
from django.views import View
# Create your views here.

def bt(request):


    return render(request,'bt/bt.html')


def btd(request):

    t = Teacher.objects.all()

    return render(request, 'bt/btd.html',{'t':t})


def df (request):

    if request.method == 'POST':
        fm = teacherRegistration(request.POST)
       
    else:
        fm = teacherRegistration()
        print('This is not a GET method')
    
    

    return render(request, 'bt/df.html',{'fm': fm})


def register(request):

    if request.method == 'POST':

        fm = UserCreationForm(request.POST)
        fm.save()
    else:
        fm = UserCreationForm()


    return render(request, 'bt/register.html', {'form':fm})


class cv(View):
    def get(self, request):
       return render(request,'bt/cv.html')