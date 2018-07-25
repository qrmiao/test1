import random
import time

from django.contrib import auth

from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render



# Create your views here.
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