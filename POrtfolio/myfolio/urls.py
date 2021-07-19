from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('<userId>/', views.index, name='myfoliohome'),
    path('<loginId>/login/', views.loginpage, name='login'),
    path('<registerId>/register/', views.registerPage, name="register"),
    path('<logoutId>/logout/', views.logoutUser, name="logout"),
    path('<editloginId>/editing/', views.savedata, name='savedata'),
    path('<editaboutId>/editing/about', views.savedataabout, name='savedataAbout'),
    path('<editskillId>/editing/skill', views.savedataskill, name='savedataskill'),
    path('<editeduId>/editing/education', views.savedataeducation, name='savedataeducation'),
    path('<editexpId>/editing/experience', views.savedataexperience, name='savedataexperience'),
    path('<editproId>/editing/project', views.savedataproject, name='savedataproject'),
    path('<editlinksId>/editing/sociallinks', views.savedatasociallinks, name='savedatasociallinks'),
]
