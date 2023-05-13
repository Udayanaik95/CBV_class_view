from django.shortcuts import render
from django.views.generic import View
from django.http import HttpResponse
from App.forms import *


# Create your views here.

# FBV for returning String.

def fbv_string(request):
    return HttpResponse('This is FBV string')

# CBV for returning String.

class cbv_string(View):
    def get(self,request):
        return HttpResponse('This is CBV string')


# FBV returning HTML page.

def fbv_html(request):
    return render(request,'fbv_html.html')  

# CBV returning HTML page. 

class cbv_html(View):
    def get(self,request):
        return render(request,'cbv_html.html')
    

# Handling forms by using FBV

def fbv_form(request):
    TFO=TopicForm()
    d={'TFO':TFO}

    if request.method == 'POST':
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')


    return render(request,'fbv_form.html',d)

# Handling forms by using CBV

class cbv_form(View):
    def get(self, request):
        TFO=TopicForm()
        d={'TFO':TFO}
        return render(request,'cbv_form.html',d)

    def post(self, request):
        TFD=TopicForm(request.POST)
        if TFD.is_valid():
            TFD.save()
            return HttpResponse('data is inserted')