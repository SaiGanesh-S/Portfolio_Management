from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader

# Create your views here.

def home_page(request):
    template = loader.get_template('home_page.html')
    return HttpResponse(template.render())