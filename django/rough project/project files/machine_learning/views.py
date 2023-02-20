from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.

def dt(request):
    d_val = {'t':200, 'a': 98.23, 'f':'book'}
    return render(request, 'machine_learning/dt.html',context=d_val)



def knn(request):
    d = {'l':[1,2,3,4,5,6,7]}
    return render(request,'machine_learning/knn.html',context = d)
