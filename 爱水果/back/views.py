import random
import time

from django.contrib import auth
from django.contrib.auth.hashers import make_password

from django.contrib.auth.models import User
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render



# Create your views here.
from user.models import UserInfo


def dj_login(request):

    if request.method == 'GET':

        return render(request, 'back/login.html')

    if request.method == 'POST':

        name = request.POST.get('username')
        password = request.POST.get('password')
        # 验证用户名和密码，通过的话，返回user对象
        user = auth.authenticate(username=name, password=password)
        if user:
            # 验证成功, 登录
            auth.login(request, user)
            return HttpResponseRedirect('/back/index/')
        else:
            return render(request, 'back/login.html')


def dj_regist(request):

    if request.method == 'GET':

        return render(request, 'back/regist.html')

    if request.method == 'POST':
        name = request.POST.get('username')
        password = request.POST.get('password')

        # if value =='1':
        User.objects.create_user(username=name, password=password)
        return HttpResponseRedirect('/back/dj_login/')
        # if value == '2':
        #     Student.objects.create(s_name = name,s_password = password)
        #     return HttpResponseRedirect('/uauth/dj_regist/')
def dj_logout(request):

    if request.method == 'GET':

        auth.logout(request)
        return HttpResponseRedirect('/back/dj_login/')

def index(request):
    return render(request, 'back/index.html')

def user_list(request):

    good = UserInfo.objects.all()
    page_id = request.GET.get('page_id', 1)
    data = {}
    paginator = Paginator(good, 4)
    page = paginator.page(int(page_id))
    data['goods'] = page
    return render(request, 'back/user_list.html', data)

def user_detail(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        if id:
            user = UserInfo.objects.get(id=id)
            return render(request, 'back/user_detail.html',{'user':user})
        return render(request, 'back/user_detail.html')
    if request.method == 'POST':
        id = request.GET.get('id')
        user = UserInfo.objects.get(id=id)
        name = request.POST.get('name')
        passwd = request.POST.get('passwd')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        address = request.POST.get('address')
        youbian = request.POST.get('youbian')
        user.uname =name
        user.upwd = make_password(passwd, salt=None)
        user.uemail = email
        user.uphone = phone
        user.uaddress = address
        user.uyoubian =youbian
        user.save()
        return render(request, 'back/user_detail.html')



