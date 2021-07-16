from django.shortcuts import render,redirect
from .models import About,Education,Experience,Projects,Skills,Social_links,Contact,loginform


# Create your views here.
def index(request,userId): 

    # About section
    abt = About.objects.filter(user_id = userId)
    
    # Quality section
    educa = Education.objects.filter(user_id=userId)
    expe = Experience.objects.filter(user_id=userId)
    edu_status =1
    exp_status =1
    if educa.exists() == False:
        edu_status = 0
        
    if expe.exists() == False:
        exp_status = 0
        
     # for Skill section
    Skl = Skills.objects.filter(user_id=userId)
    skill_status = 1
    if Skl.exists() == False:
        skill_status = 0
        
    # for portfoliio section
    proj = Projects.objects.filter(user_id = userId)

    # Contact section
    if request.method == "POST" :
        pname = request.POST.get('personname', '')
        pemail = request.POST.get('personemail', '')
        ptitle = request.POST.get('ptitle', '')
        pmsg = request.POST.get('personmsg', '')

        contact = Contact(user_id=userId,name=pname,email_Id=pemail,subject=ptitle,message=pmsg)
        contact.save()

    #social_skill  section
    sociallinks = Social_links.objects.filter(user_id = userId)
    for item in sociallinks:
        kaggle = item.kaggle_link
        fb = item.facbook_link
        insta = item.insta_link
        linkdin = item.linkdin_link
        twitter = item.twitter_link
        github  = item.github_link
        
        
    #for login modal
    # check login id exists or not and password match with it or not

    logindata = loginform.objects.filter(user_id = userId)
    for data in logindata:
        loginPass = data.user_pass
        
    
    

    data={'skill':Skl ,'skill_status': skill_status,'Edu':educa,'Exp':expe,'edu_status':edu_status,'exp_status':exp_status,'about':abt,'project':proj,'fb':fb,'kag':kaggle,'insta':insta,'linkd':linkdin,'twt':twitter,'git':github}
    return render(request,'myfolio/index.html',data)


# def login(request,userId):
    

    
    