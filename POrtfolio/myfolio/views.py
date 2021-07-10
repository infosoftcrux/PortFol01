from django.shortcuts import render
from .models import About,Education,Experience,Projects,Skills,Social_links,Others_education,Contact


# Create your views here.
def index(request):
    data={}
    return render(request,'myfolio/index.html',data)
    