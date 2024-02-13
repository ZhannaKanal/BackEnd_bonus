from __future__ import absolute_import
from sre_constants import SUCCESS
from turtle import title
from unicodedata import name
from django.shortcuts import render
from multiprocessing import context

from django.http import HttpResponse

from django.urls import reverse_lazy
from .models import *
from django.shortcuts import get_object_or_404, render, redirect, HttpResponse
from django.core.mail import send_mail
from django.core.mail import EmailMessage
from .models import Reg
from .forms import AddPostForm

# Create your views here.
from django.shortcuts import render, redirect 
from django.forms import inlineformset_factory
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import authenticate, login, logout
from django.contrib import messages
from django.contrib.auth.decorators import login_required
from .forms import CreateUserForm
from .decorators import unauthenticated_user, allowed_users
from django.contrib.auth.models import Group

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def about(request):
    footer=Footer.objects.all()
    return render(request,'posts/jabout.html',{'footer':footer})

def registration(request):
    file_data=request.FILES
    if request.method=='POST':
        form=AddPostForm(request.POST,file_data)
        # print(request.POST)
        if form.is_valid():
            #print(form.cleaned_data)
            try:
                #form.save()
                Reg.objects.create(**form.cleaned_data)
                return redirect('show_post')
            except:
                form.add_error(None,'Tapsyrys kabyldaganda kate wykty.')
    else:
        form=AddPostForm()
    return render(request,'posts/registration.html', {'title':'Tapsyrys kabyldau','form':form})
@login_required(login_url='login')
def show_post(request):
    post=Reg.objects.all().order_by('-id')[:1]
    context={'post':post}
    return render(request,'posts/post.html', context=context)

# @login_required(login_url='login')
# @admin_only
def jewelry(request):
    footer=Footer.objects.all()
    return render(request,'posts/jewelry.html',{'footer':footer})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin','student'])
def price(request):
    price1=Price1.objects.all()
    price2=Price2.objects.all()
    price3=Price3.objects.all()
    footer=Footer.objects.all()
    return render(request,'posts/jprice.html',{'footer': footer, 'price1':price1, 'price2':price2,'price3':price3})

@login_required(login_url='login')
@allowed_users(allowed_roles=['client','admin'])
def shop(request):
    footer=Footer.objects.all()    
    return render(request,'posts/jshop.html',{'footer':footer})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def contactus(request):
    footer=Footer.objects.all() 
    return render(request,'posts/jcontact.html',{'footer':footer})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def shop1(request):
    shop=Shop.objects.all()
    footer=Footer.objects.all() 
    return render(request,'posts/shop1.html',{'shop':shop,'footer':footer})

@login_required(login_url='login')
@allowed_users(allowed_roles=['admin'])
def send(request):
    # send_mail("KZHJewelry","Tapsyrys",
    #            "200103157@stu.sdu.edu.kz",
    #            ["200103157@stu.sdu.edu.kz"],
    #            fail_silently=False, html_message="<b>Your collections are awesome</b>")
    # return render(request,'posts/jewelry.html')

    email=EmailMessage("KZHJewelry","tapsyrys",
              "200103157@stu.sdu.edu.kz",
              ["kezhanna.03@mail.ru","200103157@stu.sdu.edu.kz"],
              headers={'Message-ID':'foo'},)
    email.attach_file('C:/Users/Жанна/Desktop/Front End/bonusproject/b2.jpg')
    email.send(fail_silently=False)
    return render(request,'posts/jewelry.html')  


@unauthenticated_user
def register(request):
    form = CreateUserForm()
    if request.method == 'POST':
        form = CreateUserForm(request.POST)
        if form.is_valid():
            user = form.save()
            username = form.cleaned_data.get('username')

            group = Group.objects.get(name='client')
            user.groups.add(group)

            messages.success(request, 'Account was created for ' + username)

            return redirect('login')
        

    context = {'form':form}
    return render(request, 'posts/register.html', context)

@unauthenticated_user
def loginP(request):
	if request.user.is_authenticated:
		return redirect('register')
	else:
		if request.method == 'POST':
			username = request.POST.get('username')
			password =request.POST.get('password')

			user = authenticate(request, username=username, password=password)

			if user is not None:
				login(request, user)
				return redirect('jewelry')
			else:
				messages.info(request, 'Username OR password is incorrect')

		context = {}
		return render(request, 'posts/login.html', context)


def logout(request):
	logout(request)
	return redirect('login')

