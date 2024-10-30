
from django.urls import path
from . import views

app_name = 'User'

urlpatterns = [
    path('', views.user_login,name='user_home_page'),
]