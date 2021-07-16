from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
   path('<userId>',views.index,name='myfoliohome'),
   # path('login/<userId>',views.login,name='Editfolio')
]