from django.contrib.auth.hashers import make_password, check_password
from django.shortcuts import render


from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse
from datetime import timedelta,datetime

from user.models import UserInfo, UserTicketModel
from utils.functions import get_ticket

def login(request):

    if request.method == 'GET':
        return render(request, 'un/login.html')
    if request.method == 'POST':
        username = request.POST.get('username')
        password = request.POST.get('pwd')
        user = UserInfo.objects.filter(uname=username).first()
        if user:
            if check_password(password, user.upwd):
                ticket = get_ticket()

                response = HttpResponseRedirect(reverse('user:index'))

                out_time = datetime.now() + timedelta(days=1)
                response.set_cookie('ticket', ticket, expires=out_time)
                UserTicketModel.objects.create(
                    user = user,
                    ticket =ticket,
                    out_time = out_time
                )
                return response
            else:
                return render(request, 'un/login.html', {'password': '密码错误，请重新登录！'})
        else:
            return render(request, 'un/login.html', {'name': '帐号不存在！建议先注册用户'})

def logout(request):

    if request.method == 'GET':
        response = HttpResponseRedirect(reverse('user:index'))
        ticket = request.COOKIES.get('ticket')
        response.delete_cookie('ticket')

        UserTicketModel.objects.filter(ticket=ticket).delete()

        return response

def regist(request):

    if request.method == 'GET':
        return render(request, 'un/register.html')
    if request.method == 'POST':
        username = request.POST.get('user_name')
        email = request.POST.get('email')
        password = request.POST.get('pwd')
        password1 = request.POST.get('cpwd')
        if password==password1:

            password = make_password(password, salt=None)
            # try:
            UserInfo.objects.create(uname=username,
                                    uemail=email,
                                    upwd=password,
                                     )

            return HttpResponseRedirect(reverse('user:login'))

def index(request):

    if request.method == 'GET':
        return render(request, 'un/index.html')
#用户中心
def info(request):
    if request.method == 'GET':
       user =  request.user
       return render(request, 'un/user_center_info.html',{'user':user})
def order(request):

    if request.method == 'GET':
        return render(request, 'un/user_center_order.html')
# 用户收货地址
def site(request):

    if request.method == 'GET':
        return render(request, 'un/user_center_site.html')
    if request.method == 'POST':
        user = request.user
        uname = request.POST.get('uname')
        uaddress = request.POST.get('uaddress')
        uphone = request.POST.get('uphone')
        uyoubian = request.POST.get('uyoubian')
        user.ushow = uname
        user.uaddress = uaddress
        user.uphone = uphone
        user.uyoubian = uyoubian
        user.save()
        return render(request, 'un/user_center_site.html')
def cart(request):

    if request.method == 'GET':
        return render(request, 'un/cart.html')
def place(request):

    if request.method == 'GET':
        return render(request, 'un/place_order.html')