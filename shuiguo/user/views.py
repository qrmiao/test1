from django.contrib.auth.hashers import make_password
from django.shortcuts import render


from django.contrib.auth.models import User
from django.http import HttpResponseRedirect
from django.shortcuts import render
# Create your views here.
from django.urls import reverse

from user.models import UserInfo


def login(request):

    if request.method == 'GET':
        return render(request, 'un/login.html')

def logout(request):

    if request.method == 'GET':
        return render(request, 'un/login.html')
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