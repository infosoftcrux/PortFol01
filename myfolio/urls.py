from django.urls import path
from . import views

urlpatterns = [
    path('', views.Porthome, name='home'),
    path('<userId>/', views.index, name='myfoliohome'),
    path('<loginId>/login/', views.loginpage, name='login'),
    path('<logoutId>/logout/', views.logoutUser, name="logout"),
    path('<editloginId>/editing/', views.savedata, name='savedata'),
    path('<editaboutId>/editing/about', views.savedataabout, name='savedataAbout'),
    path('<editskillId>/editing/skill', views.savedataskill, name='savedataskill'),
    path('<editeduId>/editing/education', views.savedataeducation, name='savedataeducation'),
    path('<editexpId>/editing/experience', views.savedataexperience, name='savedataexperience'),
    path('<editproId>/editing/project', views.savedataproject, name='savedataproject'),
    path('<editlinksId>/editing/sociallinks', views.savedatasociallinks, name='savedatasociallinks'),
    path('<deleteloginId>/deleting/', views.deletedata, name='deletedata'),
    path('<deleteskillId>/deleting/skill', views.deletedataskill, name='deletedataskill'),
    path('<deleteeduId>/deleting/education', views.deleteataeducation, name='deletedataeducation'),
    path('<deleteexpId>/deleting/experience', views.deletedataexperience, name='deletedataexperience'),
    path('<deleteproId>/deleting/project', views.deletedataproject, name='deletedataproject'),
    path('<passID>/changepassword/', views.changepass, name='changepass'),
    path('<passid>/resetpassword/', views.resetpass, name='resetpass'),
    path('<resetid>/<mailID>/resetpasswordPage/', views.resetpage, name='resetpage'),
]
