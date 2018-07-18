from datetime import timedelta,datetime
from random import choice
from time import time
from django.contrib.auth.hashers import make_password, check_password
from django.http import HttpResponseRedirect
from django.shortcuts import render
from django.core.urlresolvers import reverse
from user.models import UserModel,UserTicketModel
# Create your views here.
from utils.functions import get_ticket


def register(request):
    if request.method == 'GET':
        return render(request, 'user/user_register.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        email = request.POST.get('email')
        password = request.POST.get('password')

        password = make_password(password, salt=None)
        icon = request.FILES.get('icon', default='/static/img/mine.png')

        # try:
        UserModel.objects.create(username=username,
                                 email=email,
                                 password=password,
                                 icon=icon)
        # except Exception as e:
        #     return render(request, reverse('axf:register'), {'message': '用户名重复'})
        # else:
        return HttpResponseRedirect(reverse('user:login'))


def login(request):
    if request.method == 'GET':
        return render(request, 'user/user_login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('password')
        user = UserModel.objects.filter(username=username).first()
        if user:
            if check_password(password, user.password):
                ticket = get_ticket()

                response = HttpResponseRedirect(reverse('app:home'))

                out_time = datetime.now() + timedelta(days=1)
                response.set_cookie('ticket', ticket, expires=out_time)
                UserTicketModel.objects.create(
                    user = user,
                    ticket =ticket,
                    out_time = out_time
                )

                return response
            else:
                return render(request, 'user/user_login.html', {'message': '密码错误，请重新登录！'})
        else:
            return render(request, 'user/user_login.html', {'message': '帐号不存在！建议先注册用户'})

def logout(request):
    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('app:home'))
        ticket = request.COOKIES.get('ticket')
        response.delete_cookie('ticket')

        UserTicketModel.objects.filter(ticket=ticket).delete()

        return response