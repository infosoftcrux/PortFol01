from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from .forms import CreateUserForm


# Create your views here.
def index(request, userId):
    # About section
    abt = About.objects.filter(user_id=userId)

    # Quality section
    educa = Education.objects.filter(user_id=userId)
    expe = Experience.objects.filter(user_id=userId)
    edu_status = 1
    exp_status = 1
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
    proj = Projects.objects.filter(user_id=userId)

    # Contact section
    if request.method == "POST":
        pname = request.POST.get('personname', '')
        pemail = request.POST.get('personemail', '')
        ptitle = request.POST.get('ptitle', '')
        pmsg = request.POST.get('personmsg', '')

        contact = Contact(user_id=userId, name=pname,
                          email_Id=pemail, subject=ptitle, message=pmsg)
        contact.save()

        messages.success(
            request, "Thanks for contact us.I'll contact you soon...")
        return redirect('myfoliohome', userId)

    # social_skill  section
    sociallinks = Social_links.objects.filter(user_id=userId)
    kaggle = ''
    fblink = ''
    insta = ''
    linkdin = ''
    twitter = ''
    github = ''
    for item in sociallinks:
        kaggle = item.kaggle_link
        fblink = item.facbook_link
        insta = item.insta_link
        linkdin = item.linkdin_link
        twitter = item.twitter_link
        github = item.github_link

    data = {'skill': Skl, 'skill_status': skill_status, 'Edu': educa, 'Exp': expe, 'edu_status': edu_status, 'exp_status': exp_status,
            'about': abt, 'project': proj, 'fbk': fblink, 'kag': kaggle, 'insta': insta, 'linkd': linkdin, 'twt': twitter, 'git': github}
    return render(request, 'myfolio/index.html', data)


def registerPage(request, registerId):
    if request.user.is_authenticated:
        return redirect('savedata', registerId)

    else:
        form = CreateUserForm()
        if request.method == 'POST':
            form = CreateUserForm(request.POST)
            if form.is_valid():
                form.save()
                user = form.cleaned_data.get('username')
                messages.success(request, 'Account was created for ' + user)
                return redirect('login', registerId)

        abt = About.objects.filter(user_id=registerId)
        context = {'form': form, 'about': abt}
        return render(request, 'myfolio/registration.html', context)


def logoutUser(request, logoutId):
    logout(request)
    return redirect('myfoliohome', logoutId)


def loginpage(request, loginId):
    if request.user.is_authenticated:
        return redirect('savedata', loginId)
    else:
        if request.method == 'POST':
            username = request.POST.get('username')
            password = request.POST.get('password')
            user = authenticate(request, username=username, password=password)
            if user is not None:
                login(request, user)
                return redirect('savedata', loginId)
            else:
                messages.info(
                    request, 'username OR password is incorrect.please check it and try one more time')

        abt = About.objects.filter(user_id=loginId)
        return render(request, 'myfolio/login.html', {'about': abt})


@login_required
def savedata(request, editloginId):

    abut = About.objects.filter(user_id=editloginId)
    abskl = Skills.objects.filter(user_id=editloginId)
    data = {'abt': abut}
    return render(request, 'myfolio/edit.html', data)


@login_required
def savedataabout(request, editaboutId):

    if request.method == 'POST':

        # for  About section
        fname = request.POST['fname']
        lname = request.POST['lname']
        dob = request.POST['dob']
        utitle = request.POST['utitle']
        hdegree = request.POST['hdegree']
        exp = request.POST['exp']
        animetxt = request.POST['animetxt']
        phonno = request.POST['phonno']
        uemail = request.POST['uemail']
        freestatus = request.POST['freestatus']
        address = request.POST['address']
        Abot = request.POST['About']
    cvlink = request.POST['cvlink']
    About.objects.filter(user_id=editaboutId).update(user_First_name=fname, user_Second_name=lname, user_Title=utitle, user_Birthdate=dob, user_highest_degree=hdegree, user_Experience=exp,
                                                     Titles_you_want_to_show_in_animated_text_and_each_seprate_by_comma_and_oneSpace=animetxt, user_Phone_No=phonno, user_Email=uemail, user_Address=address,
                                                     user_Freelancer_status=freestatus, user_About_Desc=Abot, user_image=request.POST['pimage'], user_cv_link=cvlink)
    messages.success(request, 'Your About section data updated successflly!!')
    return redirect('savedata', editaboutId)


@login_required
def savedataskill(request, editskillId):

    # for skill section
    skillname = request.POST['skillname']
    Skillno = request.POST['Skillno']

    skillstats = Skills.objects.filter(user_Skill_name=skillname)
    if skillstats.exists():
        Skills.objects.filter(user_Skill_name=skillname, user_id=editskillId).update(
            user_skill_knows_in_percententage=Skillno)
        messages.success(
            request, 'Your skill section data updated successflly!!')
    else:
        skillcreate = Skills(user_id=editskillId, user_Skill_name=skillname,
                             user_skill_knows_in_percententage=Skillno)
        skillcreate.save()
        messages.success(
            request, 'Your skill section data created successflly!!')

    return redirect('savedata', editskillId)


@login_required
def savedataeducation(request, editeduId):

    # for education section
    eduname = request.POST['eduname']
    eduyear = request.POST['eduyear']
    educollege = request.POST['educollege']
    edudesc = request.POST['edudesc']

    edustats = Education.objects.filter(Highest_education_name=eduname)
    if edustats.exists():
        Education.objects.filter(Highest_education_name=eduname, user_id=editeduId).update(
            Highest_education_year=eduyear, Highest_education_college=educollege, Highest_education_desc=edudesc)
        messages.success(
            request, 'Your Education section data updated successflly!!')
    else:
        educreate = Education(user_id=editeduId, Highest_education_name=eduname,
                              Highest_education_year=eduyear, Highest_education_college=educollege, Highest_education_desc=edudesc)
        educreate.save()
        messages.success(
            request, 'Your Education section data created successflly!!')

    return redirect('savedata', editeduId)


@login_required
def savedataexperience(request, editexpId):

    # for experience section
    expname = request.POST['expname']
    expyear = request.POST['expyear']
    expcompony = request.POST['expcompony']
    expdesc = request.POST['expdesc']

    # edustats = Education.objects.filter(Highest_education_name=eduname)
    # if edustats.exists():
    #     Education.objects.filter(Highest_education_name=eduname, user_id=editexpId).update(
    #         Highest_education_year=eduyear, Highest_education_college=educollege, Highest_education_desc=edudesc)
    #     messages.success(
    #         request, 'Your Education section data updated successflly!!')
    # else:
    expcreate = Experience(user_id=editexpId, Experience_name=expname,
                           year_duration=expyear, compony=expcompony, Desc_about_Experience=expdesc)
    expcreate.save()
    messages.success(
        request, 'Your Education section data created successflly!!')

    return redirect('savedata', editexpId)


@login_required
def savedataproject(request, editproId):

    # for Project section
    proname = request.POST['proname']
    procat = request.POST['procat']
    proimage = request.POST['proimage']
    prolink = request.POST['prolink']
    prodesc = request.POST['prodesc']

    prostats = Projects.objects.filter(project_name=proname)
    if prostats.exists():
        Projects.objects.filter(project_name=proname, user_id=editproId).update(
            project_catagory_name=procat, project_youTubevideo_link=prolink, project_description=prodesc, project_image=proimage)
        messages.success(
            request, 'Your Projects section data updated successflly!!')
    else:
        procreate = Projects(user_id=editproId, project_name=proname,
                             project_catagory_name=procat, project_youTubevideo_link=prolink, project_description=prodesc, project_image=proimage)
        procreate.save()
        messages.success(
            request, 'Your Projects section data created successflly!!')

    return redirect('savedata', editproId)


@login_required
def savedatasociallinks(request, editlinksId):

    # for git in touch section
    linkdin = request.POST['linkdin']
    kaggle = request.POST['kaggle']
    github = request.POST['github']
    twitter = request.POST['twitter']
    facebook = request.POST['facebook']
    instagram = request.POST['instagram']

    linkstats = Social_links.objects.filter(user_id=editlinksId)

    if linkstats.exists():
        Social_links.objects.filter(user_id=editlinksId).update(kaggle_link=kaggle, github_link=github,
                                                                linkdin_link=linkdin, twitter_link=twitter, facbook_link=facebook, insta_link=instagram)
        messages.success(
            request, "Your get in touch section's data updated successflly!!")

    else:
        linkcreate = Social_links(user_id=editlinksId, kaggle_link=kaggle, github_link=github,
                                  linkdin_link=linkdin, twitter_link=twitter, facbook_link=facebook, insta_link=instagram)
        linkcreate.save()
        messages.success(
            request, 'Your get in touch links section data created successflly!!')

    return redirect('savedata', editlinksId)
