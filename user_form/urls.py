from django.urls import path
from . import views

app_name = 'user_form'

urlpatterns = [
    path('', views.UserForm, name='user'),
    path('users/', views.User_all, name='user_all'),
]
