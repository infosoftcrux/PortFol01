from django.http.response import HttpResponse
from django.shortcuts import render, redirect
from .models import *
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import user_passes_test
from .forms import CreateUserForm
from django.core.mail import send_mail
import array
import random
from django.core.signing import TimestampSigner
from django.http import Http404


# Create your views here.

def Porthome(request):
    if request.method == "POST":
        emailaddress = request.POST['email']
        userid = request.POST['user']
        getusername = request.POST['user_name']
        try:
          User.objects.get(email=emailaddress)
          messages.error(request,"This email address is already exist!!")
          return redirect('home') 
        except:
          userstatus = User.objects.filter(username=userid)
          if userstatus.exists():
            messages.error(request,"This username is already exist!!")
            return redirect('home')
          else:
            signer = TimestampSigner()
            userpass=getpass(10)
            userdata = signer.sign_object([emailaddress,userid,userpass])
            send_mail(
            f'Please!! Create My Portfolio..',
            f"Hello sir, \n\nSomeone requset you for make him portfolio, \nUser details :- \n\nUser's email address : {emailaddress} \nUser's name : {getusername} \nUser's suggestion of user name : {userid}  \n\nHere the link sir,just click this link to register User \nhttps://infosoftcrux.pythonanywhere.com/registerationofuser/{userdata}/portfolio/infosoftcrux/ \n\nFor admin login link :\nhttps://infosoftcrux.pythonanywhere.com/infosoftcruxPortfoliodatabasecreatedbymayur/ \n\nThanks & Regards",
            'infosoftcrux@gmail.com',
            ['rastogitarun9@gmail.com','shreytrivedi002@gmail.com'],
            fail_silently=False,
            )
            messages.success(request,"Thanks for registration. You'll get your userID and password within 24 hours..")
            return redirect('home')
    return render(request,'myfolio/home.html')

# @user_passes_test(lambda u: u.is_superuser)
def registerbyowner(request,userdata):
  try:
    if request.user.is_superuser:
      signer = TimestampSigner() 
      getuserdata = signer.unsign_object(userdata)
      decriptmail = getuserdata[0]
      decriptusername = getuserdata[1]
      decriptuserpass = getuserdata[2]
      decriptuserstats = User.objects.filter(username=decriptusername,email = decriptmail)
      if not decriptuserstats.exists():
        user = User.objects.create_user(decriptusername, decriptmail, decriptuserpass)
        user.save()

        usercreate = About(user_id=user, user_First_name="fdemo", user_Second_name="ldemo",
                                   user_Title="Infosoftcrux", user_Birthdate="0/0/000", user_highest_degree="hdemo", user_Experience="edemo", Titles_you_want_to_show_in_animated_text_and_each_seprate_by_comma_and_oneSpace="Demo, Infosoftcrux.com", user_Phone_No="0000000000", user_Email=decriptmail, user_Address="1234 Main St", user_Freelancer_status="not available", user_About_Desc="Our work process.Build Your Dream Projects With Us! Imagination will take us  everywhere Want to build something awesome?Just give us an idea and we will make your dream come true.We use cutting edge new technologies to deliver high quality projects." ,user_image="https://infosoftcrux.com/images/logo2.png")
        usercreate.save()
        userlinkcreate = Social_links(user_id=user)
        userlinkcreate.save()
        send_mail(
                f"Thanks for registeration | Your portfolio's Username and Password | Please do not share with anyone",
                f"Hey {user}, \n\nGreetings!! \n\nYour Portfolio has been created.\n\nYour Portfolio's Details - \nUser Id : {user} \nPassword : '{decriptuserpass}' (do not share with anyone) \n\nNow,you can just paste this userID after our website in URL And you'll get  your Portfolio very easily.\nIf you want to update your Portfolio then just login with Password and you can change anything in your portfolio from edit page.\n\nOr just click on this link : \nhttps://infosoftcrux.pythonanywhere.com/{user}/\n\n\nThanks & regards,\nInfosoftCrux Technology\ninfosoftcrux.com",
                'infosoftcrux@gmail.com',
                [decriptmail],
                fail_silently=False,
            )
        return HttpResponse("<h1 style='text-align: center; margin: auto;'>Registration Complete</h1>")
      else:
       return HttpResponse('<h1 style="text-align: center; margin: auto;">user  is already exist </h1>')
    else:
       return HttpResponse('<h1 style="text-align: center; margin: auto;">invalid registration </h1>')
  except:
    return HttpResponse('<h1 style="text-align: center; margin: auto;">Request failed </h1>')



def index(request, userId):
    # About section
    abt = About.objects.filter(user_id=userId)

    if abt.exists() == False:
        messages.error(request,"Your Portfolio dosen't exist!!. So please first register your folio then try again later!!")
        return redirect('home')
    else:
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
      pro_status = True
      if proj.exists() == False:
        pro_status = False
      

      # Contact section
      user_email = About.objects.get(user_id = userId).user_Email
      user_name = About.objects.get(user_id = userId).user_First_name
      if request.method == "POST":
         pname = request.POST.get('personname', '')
         pemail = request.POST.get('personemail', '')
         ptitle = request.POST.get('ptitle', '')
         pmsg = request.POST.get('personmsg', '')

         contact = Contact(user_id=userId, name=pname,
                          email_Id=pemail, subject=ptitle, message=pmsg)
         contact.save()
         send_mail(
            f'{pname} is Contact You Regarding "{ptitle}"',
            f"Hey {user_name}, \n\nThe visitor's Message - \n{pmsg} \n\nVistior's information - \nVisitor's name : {pname} \nVisitor's email : {pemail} \n\n\nThanks & regards,\nYour portfolio \nInfosoftCrux\ninfosoftcrux.com",
            'infosoftcrux@gmail.com',
            [user_email],
            fail_silently=False,
            )

         messages.success(request, "Thanks for contact us.I'll contact you soon...")
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

      data = {'skill': Skl, 'skill_status': skill_status, 'Edu': educa, 'Exp': expe, 'edu_status': edu_status, 'prostat':pro_status, 'exp_status': exp_status,
            'about': abt, 'project': proj, 'fbk': fblink, 'kag': kaggle, 'insta': insta, 'linkd': linkdin, 'twt': twitter, 'git': github}
      return render(request, 'myfolio/index.html', data)


def getpass(length):

    '''This function for creating any  strong paswword of any length!! '''
    max_lenth = length
    DIGITS = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9'] 
    LOCASE_CHARACTERS = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 
                     'i', 'j', 'k', 'm', 'n', 'o', 'p', 'q',
                     'r', 's', 't', 'u', 'v', 'w', 'x', 'y',
                     'z']
    UPCASE_CHARACTERS = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 
                     'I', 'J', 'K', 'M', 'N', 'O', 'p', 'Q',
                     'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y',
                     'Z']
    SYMBOLS = ['@', '#', '$']

    # combines all the character arrays above to form one array
    COMBINED_LIST = DIGITS + UPCASE_CHARACTERS + LOCASE_CHARACTERS + SYMBOLS

    # randomly select at least one character from each character set above
    rand_digit = random.choice(DIGITS)
    rand_upper = random.choice(UPCASE_CHARACTERS)
    rand_lower = random.choice(LOCASE_CHARACTERS)
    rand_symbol = random.choice(SYMBOLS)

    # combine the character randomly selected above
    # at this stage, the password contains only 4 characters
    temp_pass = rand_digit + rand_upper + rand_lower + rand_symbol

    # here we fill 6 characters also
    for x in range(max_lenth - 4):
      temp_pass = temp_pass + random.choice(COMBINED_LIST)
      temp_pass_list = array.array('u', temp_pass)
      random.shuffle(temp_pass_list)

    userpassword = ""
    for x in temp_pass_list:
        userpassword = userpassword + x

    return userpassword
      # End pasword maker


def registerPage(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            form.save()
            user = form.cleaned_data.get('username')
            email = form.cleaned_data.get('email')
            password = form.cleaned_data.get('password2')
            usercreate = About(user_id=user, user_First_name="fdemo", user_Second_name="ldemo",
                                   user_Title="Infosoftcrux", user_Birthdate="0/0/000", user_highest_degree="hdemo", user_Experience="edemo", Titles_you_want_to_show_in_animated_text_and_each_seprate_by_comma_and_oneSpace="Demo, Infosoftcrux.com", user_Phone_No="0000000000", user_Email=email, user_Address="1234 Main St", user_Freelancer_status="not available", user_About_Desc="Our work process.Build Your Dream Projects With Us! Imagination will take us  everywhere Want to build something awesome?Just give us an idea and we will make your dream come true.We use cutting edge new technologies to deliver high quality projects." ,user_image="https://infosoftcrux.com/images/logo2.png")
            usercreate.save()
            userlinkcreate = Social_links(user_id=user)
            userlinkcreate.save()
            send_mail(
                f"Thanks for registeration | Your portfolio's Username and Password | Please do not share with anyone",
                f"Hey {user}, \n\nGreetings!! \n\nYour Portfolio has been created.\n\nYour Portfolio's Details - \nUser Id : {user} \nPassword : '{password}' (do not share with anyone) \n\nNow,you can just paste this userID after our website in URL And you'll get  your Portfolio very easily.\nIf you want to update your Portfolio then just login with Password and you can change anything in your portfolio from edit page.\n\nOr just click on this link : \nhttps://infosoftcrux.pythonanywhere.com/{user}/\n\n\nThanks & regards,\nInfosoftCrux Technology\ninfosoftcrux.com",
                'infosoftcrux@gmail.com',
                [email],
                fail_silently=False,
            )
            messages.success(request, 'Portfolio has been created for ' + user)
            return redirect('register')

    return render(request, 'myfolio/registration.html',{'form':form})


def logoutUser(request, logoutId):
    logout(request)
    return redirect('myfoliohome', logoutId)

@login_required
def changepass(request,passID):
  realID = request.user.username
  if passID == realID:
    abt = About.objects.filter(user_id=passID)
    if request.method == 'POST':
        secret = request.POST['oldpass']
        newpass2 = request.POST['newpass2']
        user = authenticate(username=passID, password=secret)
        if user is not None:
            u = User.objects.get(username=passID)
            u.set_password(newpass2)
            u.save()
            messages.success(request, 'your password has been  changed')
            return redirect('login',passID)
        else:
            messages.error(request,'Your Old password is wrong!! Please enter your correct password')
            return redirect('changepass',passID)
    return render(request, 'myfolio/changepass.html', {'about':abt})
  else:
    messages.info(request, "Don't try access anyone's folio !! :| ")
    return redirect('myfoliohome' ,realID)



def loginpage(request, loginId):
    if request.user.is_authenticated:
        return redirect('savedata', loginId)
    else:
        if request.method == 'POST':
            # Email = request.POST.get('Email')
            password = request.POST.get('new_password')
            user = authenticate(request, username=loginId, password=password)
            if user is not None:
                login(request, user)
                return redirect('savedata',loginId)
            else:
                messages.info(request, "Password is incorrect. Don't try access anyone's folio !! :| ")
                return redirect('myfoliohome' ,loginId)

        abt = About.objects.filter(user_id=loginId)
        return render(request, 'myfolio/login.html', {'about': abt})


@login_required
def savedata(request, editloginId):
    passId = request.user.username
    if editloginId == passId:
      abut = About.objects.filter(user_id=editloginId)
      abskl = Skills.objects.filter(user_id=editloginId)
      abedu = Education.objects.filter(user_id=editloginId)
      abexp = Experience.objects.filter(user_id=editloginId)
      abpro = Projects.objects.filter(user_id=editloginId)
      ablink = Social_links.objects.filter(user_id=editloginId)
      data = {'abt': abut, 'skl': abskl, 'edun': abedu,
            'expce': abexp, 'prot': abpro, 'slink': ablink}
      return render(request, 'myfolio/edit.html', data)
    else:
      messages.info(request, "Don't try access anyone's folio !! :| ")
      return redirect('myfoliohome' ,passId)

@login_required
def deletedata(request,deleteloginId):
  passId = request.user.username
  if deleteloginId == passId:
    abut = About.objects.filter(user_id=deleteloginId)
    abskl = Skills.objects.filter(user_id=deleteloginId)
    abedu = Education.objects.filter(user_id=deleteloginId)
    abexp = Experience.objects.filter(user_id=deleteloginId)
    abpro = Projects.objects.filter(user_id=deleteloginId)
    data = {'abt':abut,'skl': abskl,'edun': abedu,'expce': abexp, 'prot': abpro,}

    return render(request,'myfolio/delete.html',data)
  else:
     messages.info(request, "Don't try access anyone's folio !! :| ")
     return redirect('myfoliohome' ,passId)


@login_required
def savedataabout(request, editaboutId):
  passId = request.user.username
  if editaboutId == passId:
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
    try:
     About.objects.filter(user_id=editaboutId).update(user_First_name=fname, user_Second_name=lname, user_Title=utitle, user_Birthdate=dob, user_highest_degree=hdegree, user_Experience=exp,
                                                     Titles_you_want_to_show_in_animated_text_and_each_seprate_by_comma_and_oneSpace=animetxt, user_Phone_No=phonno, user_Email=uemail, user_Address=address,
                                                     user_Freelancer_status=freestatus, user_About_Desc=Abot, user_image=request.POST['pimage'], user_cv_link=cvlink)
     messages.success(request, 'Your About section data updated successflly!!')
     return redirect('savedata', editaboutId)
    except:
        messages.error(request,'Sorry !! this Email id already exist')
        return redirect('savedata', editaboutId)


@login_required
def savedataskill(request, editskillId):
  passId = request.user.username
  if editskillId == passId:

    # for skill section
    skillname = request.POST['skillname']
    Skillno = request.POST['Skillno']

    skillstats = Skills.objects.filter(user_id=editskillId,user_Skill_name=skillname)
    if skillstats.exists():
        Skills.objects.filter(user_Skill_name=skillname, user_id=editskillId).update(user_skill_knows_in_percententage=Skillno)
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
def deletedataskill(request,deleteskillId):
  passId = request.user.username
  if deleteskillId == passId:
     # for skill section
    skillname = request.POST['skillname']
    skill = Skills.objects.filter(user_id=deleteskillId, user_Skill_name=skillname)
    skill.delete()
    messages.success( request, f'Your {skillname} skill deleted successflly!!')
    return redirect('deletedata',deleteskillId )




@login_required
def savedataeducation(request, editeduId):
  passId = request.user.username
  if editeduId == passId:
    # for education section
    eduname = request.POST['eduname']
    eduyear = request.POST['eduyear']
    educollege = request.POST['educollege']
    edudesc = request.POST['edudesc']

    edustats = Education.objects.filter(user_id=editeduId,Highest_education_name=eduname)
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
def deleteataeducation(request,deleteeduId):
  passId = request.user.username
  if deleteeduId == passId:
     # for education section
    eduname = request.POST['eduname']
    edus = Education.objects.filter(user_id=deleteeduId,Highest_education_name=eduname)
    edus.delete()
    messages.success( request, f'Your {eduname} Education deleted successflly!!')
    return redirect('deletedata',deleteeduId )

@login_required
def savedataexperience(request, editexpId):
  passId = request.user.username
  if editexpId == passId:
    # for experience section
    expname = request.POST['expname']
    expyear = request.POST['expyear']
    expcompony = request.POST['expcompony']
    expdesc = request.POST['expdesc']

    expcreate = Experience(user_id=editexpId, Experience_name=expname,
                           year_duration=expyear, compony=expcompony, Desc_about_Experience=expdesc)
    expcreate.save()
    messages.success(
        request, 'Your Education section data created successflly!!')

    return redirect('savedata', editexpId)


@login_required
def deletedataexperience(request,deleteexpId):
  passId = request.user.username
  if deleteexpId == passId:
     # for experience section
    expname = request.POST['expname']
    exper = Experience.objects.filter(user_id=deleteexpId,Experience_name=expname)
    exper.delete()
    messages.success( request, f'Your {expname} Experience deleted successflly!!')
    return redirect('deletedata',deleteexpId )


@login_required
def deletedataproject(request,deleteproId):
  passId = request.user.username
  if deleteproId == passId:
     # for Project section
    proname = request.POST['proname']
    pros = Projects.objects.filter(user_id=deleteproId,project_name=proname)
    pros.delete()
    messages.success( request, f'Your {proname} Project deleted successflly!!')
    return redirect('deletedata',deleteproId )

@login_required
def savedataproject(request, editproId):
  passId = request.user.username
  if editproId == passId:
    # for Project section
    proname = request.POST['proname']
    procat = request.POST['procat']
    proimage = request.POST['proimage']
    prolink = request.POST['prolink']
    prodesc = request.POST['prodesc']

    prostats = Projects.objects.filter(user_id=editproId,project_name=proname)
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
  passId = request.user.username
  if editlinksId == passId:
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

def resetpass(request,passid):
   user_name = About.objects.get(user_id = passid).user_First_name
  
   if request.method == 'POST':
       useremail  = request.POST['usermail']
       try:
           authid = User.objects.get(username = passid,email=useremail)
           
           try:
             Otp = random.randrange(000000,999999)
             signer = TimestampSigner() 
             mail = signer.sign_object([useremail])
             send_mail(
               "!!RESET PASSWORD!! | OTP | Don't share with anyone",
               f"Hey {user_name}, \n\nWe have received a request to reset your portfolio password !!! \nYour OTP is ' {Otp} ' (please don't share!) \n\n\nThanks & regards,\nYour portfolio \nInfosoftCrux\ninfosoftcrux.com",
                'infosoftcrux@gmail.com',
                [useremail],
                fail_silently=False)
             mailstatus= OTPRESET.objects.filter(email=useremail)
             if mailstatus.exists():
                    OTPRESET.objects.filter(email=useremail).update(otp=Otp)
             else:
                 otpmodelcreate = OTPRESET(email=useremail,otp=Otp)
                 otpmodelcreate.save()
             request.session['resetpass']= 'resetpassword'
             request.session.set_expiry(300)
             
             messages.success(request,'OTP has been send to your email')
             return redirect('resetpage',resetid = authid,mailID = mail)
           except:
             messages.error(request,'Something went wrong')
             return redirect('resetpass',passid)
       except:
           messages.error(request,'Wrong email!! Please enter your registered email id !!')
           return redirect('resetpass',passid)
   args ={'id':passid}
   return render(request, 'myfolio/reset.html',args)

def resetpage(request,resetid,mailID):
      signer = TimestampSigner() 
      getemail = signer.unsign_object(mailID)
      decriptmail = getemail[0]
      try:
         authid = User.objects.get(username = resetid,email=decriptmail)
         savedotp = OTPRESET.objects.get(email=decriptmail).otp
        #  savedtime = OTPRESET.objects.get(email=decriptmail).otp
         if request.method == 'POST':
           if 'resetpass' in request.session:
             enterotp = request.POST['otp']
             newpass  = request.POST['newpass2']
             if enterotp == savedotp:
               u = User.objects.get(username=authid)
               u.set_password(newpass)
               u.save()
               OTPRESET.objects.filter(email=decriptmail).delete()
               messages.success(request, 'your password has been  Reset!!')
               request.session.flush()
               request.session.clear_expired()
               return redirect('myfoliohome',authid)
             else:
               messages.error(request, 'This OTP is wrong !!!!')
               return redirect('resetpage',resetid= authid,actualID=mailID)
           else:
              messages.info(request,'Your session has been expired!!')
              return redirect('resetpass',authid)
      except:
          raise Http404("Page does not exist")
      args ={'id':resetid,'useid':mailID}
      return render(request, 'myfolio/resetpage.html',args)