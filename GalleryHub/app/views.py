from django.shortcuts import render,redirect

from django.contrib.auth import authenticate,login,logout
from . models import *
import os
from django.contrib.auth.models import User
from django.contrib import messages
# Create your views here.

def user_login(req):
  
   

    if req.method=='POST':
        uname=req.POST['uname']
    
        password=req.POST['password']
        data=authenticate(username=uname,password=password)
        if data:
            login(req,data)    
            req.session['user']=uname
            return redirect(index)
        else:
            messages.warning(req, "Invalid Username or Password")
            return redirect(user_login)
    else:
        return render(req,'login.html')    

        
def shop_logout(req):
    logout(req)
    req.session.flush()
    return redirect(user_login)

def register(req):
    if req.method=='POST':
        name=req.POST['name']
        email=req.POST['email']
        password=req.POST['password']
        try:
            data=User.objects.create_user(first_name=name,username=email,email=email,password=password)
            data.save()
            return redirect(user_login)
        except:
            messages.warning(req,"user details already exits.")
            return redirect(register)
    else:
        return render(req,'register.html')
    


def index(req):
    if 'user' in req.session:
        # data=UploadedFile.objects.all()
        # return render(req,'index.html',{'file':data})
    # else:
        return render(req,'home.html')

def images(req):
    data=Image.objects.all()
    return render(req,'img.html',{'image':data})

def video(req):
    data=Video.objects.all()
    return render(req,'vdo.html',{'video':data})

def audio(req):
    data=Audio.objects.all()
    return render(req,'odo.html',{'audio':data})



def add_img(req):
    if req.method=='POST':
        title=req.POST['title']
        des=req.POST['description']
        # price=req.POST['price']
        img=req.FILES['image_file']
        data=Image.objects.create(title=title,description=des,image_file=img)
        data.save()
        return redirect(images)
    return render(req,'add_img.html')

def delete_img(req,id):
    data=Image.objects.get(pk=id)
    url=data.image_file.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(images)


def add_vdo(req):
    if req.method=='POST':
        title=req.POST['title']
        des=req.POST['description']
        # price=req.POST['price']
        vdo=req.FILES['video_file']
        data=Video.objects.create(title=title,description=des,video_file=vdo)
        data.save()
        return redirect(video)
    return render(req,'add_vdo.html')

def delete_vdo(req,id):
    data=Video.objects.get(pk=id)
    url=data.video_file.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(video)

def add_odo(req):
    if req.method=='POST':
        title=req.POST['title']
        des=req.POST['description']
        # price=req.POST['price']
        odo=req.FILES['audio_file']
        data=Audio.objects.create(title=title,description=des,audio_file=odo)
        data.save()
        return redirect(audio)
    return render(req,'add_odo.html')

def delete_odo(req,id):
    data=Audio.objects.get(pk=id)
    url=data.audio_file.url
    url=url.split('/')[-1]
    os.remove('media/'+url)
    data.delete()
    return redirect(audio)