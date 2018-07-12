from django.contrib.auth.hashers import make_password, check_password
from django.core.paginator import Paginator
from django.http import HttpResponseRedirect

import random
import time

from django.core.urlresolvers import reverse
from django.shortcuts import render

from commodity.models import sweaters, sweater, women, Img
from stu.filters import StuFilter
from stu.models import Student, StudentInfo, StudentShop, MyUser,Promission,My_Role

import logging

from rest_framework import mixins, viewsets
from stu.serializers import StudentSerializer

logger = logging.getLogger('stu')


# def index(request):
#
#     if request.method == 'GET':
#         # 获取所有学生信息
#         # ticket = request.COOKIES.get('ticket')
#         # if not ticket:
#         #     return HttpResponseRedirect('/uauth/login/')
#         # if Users.objects.filter(u_ticket=ticket).exists():
#         #     stuinfos = StudentInfo.objects.all()
#         #     return render(request, 'index.html', {'stuinfos':stuinfos})
#         # else:
#         #     return HttpResponseRedirect('/uauth/login/')
#
#         stuinfos = StudentInfo.objects.all()
#         logger.info('url: %s method:%s 获取学生信息成功' % (request.path, request.method))
#         return render(request, 'index.html', {'stuinfos': stuinfos})
#
#
# def addStu(request):
#
#     if request.method == 'GET':
#
#         return render(request, 'addStu.html')
#
#     if request.method == 'POST':
#         # 跳转到学习详情方法中去
#         name = request.POST.get('name')
#         tel = request.POST.get('tel')
#
#         stu = Student.objects.create(s_name=name, s_tel=tel)
#
#         return HttpResponseRedirect(
#             reverse('s:addinfo', kwargs={'stu_id': stu.id})
#         )
#
#
# def addStuInfo(request, stu_id):
#
#     if request.method == 'GET':
#
#         return render(request, 'addStuInfo.html', {'stu_id':stu_id})
#
#     if request.method == 'POST':
#
#         stu_id = request.POST.get('stu_id')
#         addr = request.POST.get('addr')
#
#         # 添加头像图片
#         img = request.FILES.get('img')
#
#         StudentInfo.objects.create(i_addr=addr, s_id=stu_id, i_image=img)
#
#         return HttpResponseRedirect('/stu/index/')
#
#
# def aStuPage(request):
#
#     if request.method == 'GET':
#
#         page_num = request.GET.get('page_num', 1)
#         stus = Student.objects.all()
#         paginator = Paginator(stus, 2)
#         page = paginator.page(int(page_num))
#         return render(request, 'stupage.html', {'page': page})
#
# def stuPage(request):
#
#     if request.method == 'GET':
#         page_id = request.GET.get('page_id', 1)
#         stus = Student.objects.all()
#         paginator = Paginator(stus, 3)
#         page = paginator.page(int(page_id))
#         return render(request, 'index_page.html', {'stus': page})

def regist(request):

    if request.method == 'GET':

        return render(request, 'new/account.html')

    if request.method == 'POST':
        # 注册
        name = request.POST.get('name')
        email = request.POST.get('email')
        password1 = request.POST.get('password1')
        password2 = request.POST.get('password2')
        if password1 == password2:

            password = make_password(password1)

            Student.objects.create(s_name=name,
                                 s_password=password ,s_emil = email)
            return HttpResponseRedirect('/stu/login/')

def login(request):

    if request.method == 'GET':

        return render(request, 'new/login.html')

    if request.method == 'POST':
        # 如果登录成功，绑定参数到cookie中，set_cookie
        name = request.POST.get('name')
        password = request.POST.get('password')

        if Student.objects.filter(s_name=name).exists():
            student = Student.objects.get(s_name=name)
            if check_password(password, student.s_password):
                s = 'qwertyuiopasdfghjklzxcvbnm1234567890'
                ticket = ''
                for i in range(15):
                    # 获取随机的字符串
                    ticket += random.choice(s)
                now_time = int(time.time())
                ticket = 'TK_' + ticket + str(now_time)
                # ticket = 'agdoajbfjad'
                # 绑定令牌到cookie里面
                # response = HttpResponse('登录成功')


                response = HttpResponseRedirect('/comm/index' )
                # max_age 存活时间
                response.set_cookie('ticket', ticket , max_age=50)
                # 存在服务段
                student.s_ticket = ticket
                student.save()
                return response
            else:
                # return HttpResponse('用户密码错误')
                return render(request, 'new/login.html', {'password': '用户密码错误'})
        else:
            # return HttpResponse('用户不存在')
            return render(request, 'new/login.html', {'name':'用户不存在'})

def logout(request):

    if request.method == 'GET':
        response = HttpResponseRedirect('/stu/login/')
        response.delete_cookie('ticket')
        return response
class StudentEdit(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    # 查询所有信息
    queryset = Student.objects.all()
    # 序列化
    serializer_class = StudentSerializer
    filter_class = StuFilter
def test(request):
    return render(request, 'index.html')

def index(request):
    return render(request, 'new/index.html')
def product(request):
    return render(request, 'new/product.html')
def lalal(request):
    if request.method == 'GET':
        id = request.GET.get('id')

        my_products =sweater.objects.get(id=id).sweaters_set.all()

        return render(request, 'new/register.html',{'my_products':my_products})
def top(request):
    return render(request, 'top.html')
def bottom(request):
    return render(request, 'bottom.html')
def swich(request):
    return render(request, 'swich.html')
def left(request):
    return render(request, 'left.html')
def main(request):
    return render(request, 'main.html')
def add(request):
    return render(request, 'main_info.html')
def main_list(request):
    if request.method == 'GET':
        page_id = request.GET.get('page_id', 1)
        stu = Student.objects.all()
        sum = Student.objects.all().count()
        paginator = Paginator(stu, 3)
        page = paginator.page(int(page_id))

        return render(request, 'main_list.html',{'stus': page,'sum':sum})
            # logger.info('url: %s method:%s 获取学生信息成功' % (request.path, request.method))

def ddel(request):
    if request.method == 'GET':
        del_id = request.GET.get('del_id')
        Student.objects.filter(id=del_id).delete()

        return HttpResponseRedirect('/stu/main_list')

def main_in(request):
    if request.method == 'GET':
        del_id = request.GET.get('id')
        stu = Student.objects.get(id=del_id)

        return render(request, 'main_in.html', {'stu': stu, })
    if request.method == 'POST':
        id =  request.GET.get('id')
        name = request.POST.get('name')
        password = request.POST.get('password')
        email = request.POST.get('email')
        time = request.POST.get('time')
        stu = Student.objects.get(id=id)
        stu.s_name = name
        stu.s_password = password
        stu.s_emil = email
        stu.s_operate_time = time
        stu.save()
        return HttpResponseRedirect('/stu/main_list')
def main_menu(request):
    if request.method == 'GET':

        stu = women.objects.all()

        return render(request,  'main_menu.html', {'stu': stu, })
def main_change(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        id1 =  request.GET.get('sid')
        if id:
            stu = women.objects.get(id=id)
            name = stu.w_name

            return render(request, 'main_change.html', {'stu': stu,'name':name })
        if id1:
            stu = sweater.objects.get(id=id1)
            name = stu.sw_name

            return render(request, 'main_change.html', {'stu': stu,'name':name })


    if request.method == 'POST':

        id1 = request.GET.get('id')
        id2 = request.GET.get('sid')
        if id1:
            name = request.POST.get('name')
            stu = women.objects.get(id=id1)
            stu.id = id1
            stu.w_name = name
            stu.save()
            return HttpResponseRedirect('/stu/main_menu')
        if id2:
            name = request.POST.get('name')
            stu = sweater.objects.get(id=id2)
            stu.id = id2
            stu.sw_name = name
            stu.save()
            return HttpResponseRedirect('/stu/main_menu')

def main_menu_next(request):
    if request.method == 'GET':
        id = request.GET.get('id')

        stu = women.objects.get(id = id).sweater_set.all()

        return render(request,  'main_menu_next.html', {'stu': stu,'wid':id })
def main_add(request):
    if request.method == 'GET':

        return render(request,  'main_add.html')
    if request.method == 'POST':
        id1 = request.GET.get('wid')

        id2 = request.POST.get('id')
        name = request.POST.get('name')
        stu = sweater.objects.create(id = id2,sw_name = name,s_id =id1)
        stu.save()
        return HttpResponseRedirect('/stu/main_menu')

def main_menu_last(request):
    if request.method == 'GET':
        id = request.GET.get('id')

        stu = sweater.objects.get(id = id).sweaters_set.all()

        return render(request,  'main_menu_last.html', {'stu': stu,'wid':id })
def main_menu_add(request):
    if request.method == 'GET':


        return render(request,  'main_menu_add.html',)
    if request.method == 'POST':
        id1 = request.GET.get('wid')
        sws_name = request.POST.get('sws_name')
        sws_pic = request.POST.get('sws_pic')
        sws_num = request.POST.get('sws_num')
        sws_introduction = request.POST.get('sws_introduction')
        sws_img = request.FILES.get('sws_img')
        sws_img1 = request.FILES.get('sws_img1')
        sws_img2 = request.FILES.get('sws_img2')
        stu = sweaters.objects.create(sws_name = sws_name,sws_pic = sws_pic, sws_num =sws_num, sws_introduction= sws_introduction,sws_img = sws_img,sws_img1= sws_img1,sws_img2 = sws_img2,ss_id=id1)
        stu.save()
        return HttpResponseRedirect('/stu/main_menu')
def main_menu_del(request):
    if request.method == 'GET':
        id1 = request.GET.get('s_id')
        id2 = request.GET.get('sws_id')
        if id1:
            sweater.objects.filter(id=id1).delete()
        if id2:
            sweaters.objects.filter(id=id2).delete()

        return HttpResponseRedirect('/stu/main_menu')


def main_menu_change(request):
    if request.method == 'GET':
        id = request.GET.get('id')

        stu = sweaters.objects.get(id = id)

        return render(request,  'main_menu_change.html', {'stu': stu, })
    if request.method == 'POST':
        id = request.GET.get('id')

        sws_name = request.POST.get('sws_name')
        sws_pic = request.POST.get('sws_pic')
        sws_num = request.POST.get('sws_num')
        sws_introduction = request.POST.get('sws_introduction')
        sws_img = request.FILES.get('sws_img')
        sws_img1 = request.FILES.get('sws_img1')
        sws_img2 = request.FILES.get('sws_img2')
        stu = sweaters.objects.get(id=id)
        stu.sws_name = sws_name
        stu.sws_pic = sws_pic
        stu.sws_num = sws_num
        stu.sws_introduction = sws_introduction
        if sws_img:
            stu.sws_img = sws_img
        if sws_img:
            stu.sws_img1 = sws_img1
        if sws_img:
            stu.sws_img2 = sws_img2


        stu.save()
        return HttpResponseRedirect('/stu/main_menu')
def main_message(request):

    if request.method == 'GET':
        page_id = request.GET.get('page_id', 1)
        stu =StudentShop.objects.all()
        sum = stu.count()
        paginator = Paginator(stu, 3)
        page = paginator.page(int(page_id))

        # return render(request, 'main_list.html', {'stus': page, 'sum': sum})

        return render(request, 'main_message.html', {'stu': page,'sum': sum})

def message_info(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        stu = StudentShop.objects.get(id=id)
        return render(request, 'message_info.html', {'stu': stu})

def message_replay(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        stu =StudentShop.objects.get(id = id)
        return render(request, 'message_replay.html', {'stu': stu})
    if request.method == 'POST':
        id = request.GET.get('id')
        stu =StudentShop.objects.get(id = id)
        num =request.POST.get('num')
        size = request.POST.get('size')
        zh = request.POST.get('zh')
        stu.sis_num = num
        stu.sis_size = size
        stu.sis_zh = zh
        stu.save()

        return HttpResponseRedirect('/stu/main_message')

def message_del(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        StudentShop.objects.get(id = id).delete()
        return HttpResponseRedirect('/stu/main_message')

def message_ok(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        stu = StudentShop.objects.get(id = id)
        stu.sis_zh='已处理'
        stu.save()
        return HttpResponseRedirect('/stu/main_message')
def test(request):
    if request.method =='GET':
        user = MyUser.objects.get(id = 1).my
        ab = user.my_p.all()
        cc = [i.p_name for i in ab]
        pu = Promission.objects.get(p_name ='add')
        ma = pu.my_role_set.all()

        for i in range(len(ma)):
            for j in ma :
                lala = [j.myuser_set.all()[i].my_name]
        return render(request, 'test.html', {'lala': lala})




