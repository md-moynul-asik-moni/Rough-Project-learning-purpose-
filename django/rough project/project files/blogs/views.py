from django.shortcuts import render
from django.http import HttpResponse

# Create your views here.


def blog1(request):

    return HttpResponse('This is from blog1 function of blog app')