from django.shortcuts import render
from django.http import HttpResponse
from django.template import loader
# Create your views here.

def user_login(request):
    template = loader.get_template('create_user.html')
    return HttpResponse(template.render())