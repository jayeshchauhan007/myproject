from django.shortcuts import render,HttpResponseRedirect
from .models import *
from django.core.mail import send_mail
from .utils import sendmail
from random import *

# Create your views here.

def index(request):
    if "email" in request.session:
        uid=Student.objects.get(email=request.session['email'])
        data=Blog.objects.all()
        return render(request,'myapp/index.html',{'uid':uid,'data':data})
    else:
        return render(request,'myapp/index.html')

def loginpage(request):
    if "email" in request.session:
        uid=Student.objects.get(email=request.session['email'])
        return render(request,'myapp/index.html',{'uid':uid})
    else:
        return render(request,'myapp/login.html')

def registrationpage(request):
    if "email" in request.session:
        uid=Student.objects.get(email=request.session['email'])
        return render(request,'myapp/index.html',{'uid':uid})
    else:
        return render(request,'myapp/registration.html')

def register(request):
    try:
        if "username" in request.POST:
            u_name=request.POST['username']
            u_email=request.POST['email']
            u_password=request.POST['password']

            uid=Student.objects.create(username=u_name,email=u_email,password=u_password)

            if uid:
                print("Successfully Register")
                smsg="Successfully Register"
                subject="confirmation mail"
                #send_mail(subject,smsg,"jc84250@gmail.com",[u_email])
                sendmail(subject,"mail_template",u_email,{'u_name':u_name,'u_email':u_email})
                return render(request,'myapp/registration.html',{'smsg':smsg})
            else:
                print("error")
                emsg="error"
                return render(request,'myapp/registration.html',{'emsg':emsg})
        else:
            return render(request,'myapp/registration.html')
    except:
        print("already exist")
        emsg="already exist"
        return render(request,'myapp/registration.html',{'emsg':emsg})

def login(request):
    if "email" in request.session:
        return render(request,'myapp/index.html')
    else:
        try:
            u_email=request.POST['email']
            u_password=request.POST['password']
            uid=Student.objects.filter(email=u_email)

            if uid:
                if uid[0].password==u_password:
                    request.session['username']=uid[0].username
                    request.session['email']=uid[0].email
                    """if request.POST.get("chk"):
                        response=HttpResponseRedirect(reverse('login-page'))
                        max_age=360*24*60*60
                        response.set_cookie('email',request.POST['email'],max_age)
                        response.set_cookie('password',request.POST['password'],max_age)
                        return response
                    else:
                        response=HttpResponseRedirect(reverse('login-page'))
                        response.delete_cookie('email')
                        response.delete_cookie('password')
                        return response"""
                    uid=Student.objects.get(email=request.session['email'])
                    return render(request,'myapp/index.html',{'uid':uid})
            else:
                e_msg="Else part"
                return render(request,'myapp/login.html',{'e_msg':e_msg})
        except:
            e_msg="Invalid email or password"
            return render(request,'myapp/login.html',{'e_msg':e_msg})

def logout(request):
    if "email" in request.session:
        del request.session["email"]
        del request.session["username"]
        return render(request,'myapp/login.html')
    else:
        return render(request,'myapp/login.html')

def edit_profile(request):
    if "email" in request.session:
        uid=Student.objects.get(email=request.session['email'])
        return render(request,'myapp/profile.html',{'uid':uid})
    else:
        return render(request,'myapp/login.html')

def update_profile(request):
    if "email" in request.session:
        username=request.POST['username']
        email=request.POST['email']
        password=request.POST['password']
        contact=request.POST['contact']
        profile_pic=request.FILES['img']

        uid=Student.objects.get(email=request.session['email'])

        uid.username=username
        uid.email=email
        uid.password=password
        uid.contacts=contact
        uid.profile_pic=profile_pic

        uid.save()
        request.session['username']=uid.username    
        return render(request,'myapp/index.html')
    else:
        return render(request,'myapp/login.html')

def forgot_password(request):
    return render(request,'myapp/forgot_password.html')

def send_otp(request):
    try:
        email=request.POST['email']
        uid=Student.objects.get(email=email)
        if uid:
            otp=randint(1111,9999)
            uid.otp=otp
            uid.save()
            context={
                'u_name':uid.username,
                'email':email,
                'otp':otp
            }
            sendmail("forgot password","otp_mail",email,{'context':context})
            return render(request,'myapp/reset_password.html',{'email':email})
        else:
            e_msg="Invalid email or password"
            return render(request,'myapp/forgot_password.html',{'e_msg':e_msg})
    except:
        e_msg="Invalid email or password"
        return render(request,'myapp/forgot_password.html',{'e_msg':e_msg})

def reset_password(request):
    try:
        email=request.POST['email']
        otp=request.POST['otp']
        newpassword=request.POST['newpassword']
        retypepassword=request.POST['retypepassword']
        uid=Student.objects.get(email=email)
        if uid:
            if str(uid.otp)==otp and newpassword==retypepassword:
                uid.password=newpassword
                uid.save()
                otp=randint(1111,9999)
                uid.otp=otp
                uid.save()
                return render(request,'myapp/login.html')
            else:
                e_msg="Invalid otp or password"
                return render(request,'myapp/login.html',{'e_msg':e_msg})
    except:
        e_msg="Invalid otp or password"
        return render(request,'myapp/forgot_password.html',{'e_msg':e_msg})

def recipes(request):
    if "email" in request.session:
        data=Blog.objects.all()
        return render(request,'myapp/recipes.html',{'data':data})
    else:
        return render(request,'myapp/login.html')

def recipe_single(request):
    if "email" in request.session:
        data=Blog.objects.all()
        return render(request,'myapp/recipe-single.html',{'data':data})
    else:
        return render(request,'myapp/login.html')

def reviews(request):
    if "email" in request.session:
        return render(request,'myapp/reviews.html')
    else:
        return render(request,'myapp/login.html')

def contact(request):
    if "email" in request.session:
        return render(request,'myapp/contact.html')
    else:
        return render(request,'myapp/login.html')

def about(request):
    if "email" in request.session:
        return render(request,'myapp/about.html')
    else:
        return render(request,'myapp/login.html')

def subscribe(request):
    if "email" in request.session:
        n_email=request.POST['email']
        nid=Newsletter.objects.create(email=n_email)
        return render(request,'myapp/about.html')
    else:
        return render(request,'myapp/login.html')

def send_comment(request):
    if "email" in request.session:
        u_name=request.POST['name']
        u_email=request.POST['email']
        subject=request.POST['subject']
        message=request.POST['message']
        send_mail(subject,message,u_email,['jc814250@gmail.com'])
        return render(request,'myapp/contact.html')
    else:
        return render(request,'myapp/login.html')

def add_blog(request):
    if "email" in request.session:
        title=request.POST['title']
        description=request.POST['description']
        date=request.POST['date']
        pic=request.FILES['pic']
        bid=Blog.objects.create(title=title,description=description,date=date,pic=pic)
        return render(request,'myapp/index.html')
    else:
        return render(request,'myapp/login.html')