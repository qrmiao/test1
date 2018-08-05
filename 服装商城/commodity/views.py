from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render
from rest_framework import mixins, viewsets
# Create your views here.
from commodity import Serializer, SweatersFilter
from commodity.Serializer import SweatersSerializer, SweaterSerializer
from commodity.models import sweaters, sweater, women
from stu.models import StudentInfo, Student, StudentShop
from utils.fun import is_login


class Show(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    # 查询所有信息
    queryset = sweaters.objects.all()
    # 序列化
    serializer_class = SweatersSerializer
    # filter_class = SweatersFilter
class Shop(mixins.ListModelMixin,
                  mixins.RetrieveModelMixin,
                  mixins.UpdateModelMixin,
                  mixins.DestroyModelMixin,
                  mixins.CreateModelMixin,
                  viewsets.GenericViewSet):

    # 查询所有信息
    queryset = sweater.objects.all()
    # 序列化
    serializer_class = SweaterSerializer
    # filter_class = SweatersFilter
def product(request):
    if request.method == 'GET':
        tk = request.COOKIES.get('ticket')

        if tk:
            id = request.GET.get('id')
            sid = request.GET.get('sid')
            if id:

                st = women.objects.get(id=id).sweater_set.all()
                name = Student.objects.get(s_ticket=tk).s_name
                stus = []
                for st_sub in st:
                    stus += st_sub.sweaters_set.all()
                stu = women.objects.all()
                page_id = request.GET.get('page_id', 1)

                paginator = Paginator(stus, 3)
                page = paginator.page(int(page_id))

                lala = Student.objects.get(s_name=name).studentinfo_set.all()
                all = lala.count()

                sum = 0
                for s in lala:
                    sum += s.si_pic
                dent = {'stus': page, 'stu': stu, 'st': st, 'name': name,'all':all,'sum':sum,'id':id}
                return render(request, 'new/product.html', dent)
            if sid:
                ### 所有商品
                stus = sweater.objects.get(id=sid).sweaters_set.all()
                la = sweater.objects.get(id=sid).s_id
                st = sweater.objects.filter(s_id = la)
                name = Student.objects.get(s_ticket=tk).s_name
                stu = women.objects.all()
                lala = Student.objects.get(s_name=name).studentinfo_set.all()
                all = lala.count()
                page_id = request.GET.get('page_id', 1)
                paginator = Paginator(stus, 3)
                page = paginator.page(int(page_id))
                sum = 0
                for s in lala:
                    sum += s.si_pic
                dent = {'stus': page, 'stu': stu, 'st': st, 'name': name,'all':all,'sum':sum,'sid':sid}
                return render(request, 'new/product.html', dent)
        else:
            id = request.GET.get('id')
            sid = request.GET.get('sid')
            if id:

                st = women.objects.get(id=id).sweater_set.all()

                stus = []
                for st_sub in st:
                    stus += st_sub.sweaters_set.all()
                stu = women.objects.all()
                page_id = request.GET.get('page_id', 1)

                paginator = Paginator(stus, 3)
                page = paginator.page(int(page_id))



                dent = {'stus': page, 'stu': stu, 'st': st, 'id':id}
                return render(request, 'new/product.html', dent)
            if sid:
                ### 所有商品
                stus = sweater.objects.get(id=sid).sweaters_set.all()
                la = sweater.objects.get(id=sid).s_id
                st = sweater.objects.filter(s_id = la)

                stu = women.objects.all()

                page_id = request.GET.get('page_id', 1)
                paginator = Paginator(stus, 3)
                page = paginator.page(int(page_id))

                dent = {'stus': page, 'stu': stu, 'st': st,'sid':sid}
                return render(request, 'new/product.html', dent)





@is_login
def index(request):
    if request.method == 'GET':
        tk = request.COOKIES.get('ticket')
        if tk :
            name = Student.objects.get(s_ticket=tk).s_name
            stus = women.objects.all()

            lala = Student.objects.get(s_name=name).studentinfo_set.all()
            all = lala.count()

            sum = 0
            for st in lala:
                sum += st.si_pic
            stu = {'stu': stus, 'name': name,'sum':sum,'all':all}
            return render(request, 'new/index.html', stu)
        stu = women.objects.all()


        return render(request, 'new/index.html',{'stu':stu})

# def indexin(request,name):
#     if request.method == 'GET':
#
#
#
#         stu = women.objects.all()
#         stus = { 'stu':stu,'name':name}
#
#
#         return render(request, 'new/index.html',stus)



def car(request):
    if request.method == 'GET':
        tk = request.COOKIES.get('ticket')
        if tk:
            stus = women.objects.all()
            name = Student.objects.get(s_ticket=tk).s_name
            page_id = request.GET.get('page_id', 1)
            stu = Student.objects.get(s_name=name).studentinfo_set.all()
            all = stu.count()
            paginator = Paginator(stu, 1)
            page = paginator.page(int(page_id))
            num =0
            sum = 0
            for st in stu:
                sum +=st.si_pic
                num +=st.si_num

            return render(request, 'new/checkout.html', { 'stus':stus,'stu': page, 'num': num, 'name': name, 'sum': sum, 'all': all})
        return HttpResponseRedirect('/stu/login/')
def dell(request):
    if request.method == 'GET':
        tk = request.COOKIES.get('ticket')
        if tk:
            id = request.GET.get('id')
            StudentInfo.objects.get(id  =id).delete()
            return HttpResponseRedirect('/comm/car/')
def single(request):
    if request.method == 'GET':
        tk = request.COOKIES.get('ticket')
        if tk :

            name = Student.objects.get(s_ticket=tk).s_name
            stus = women.objects.all()
            id = request.GET.get('id')
            na = sweaters.objects.get(id = id)
            ma = sweater.objects.get(id = na.ss_id).s_id
            stu =sweater.objects.filter(s_id = ma)
            lala = Student.objects.get(s_name=name).studentinfo_set.all()
            all = lala.count()
            sum = 0
            for st in lala:
                sum += st.si_pic
            stu = {'stu': stus, 'name': name,'sum':sum,'all':all ,'stus':stu,'na':na}
            return render(request, 'new/single.html', stu)
        return HttpResponseRedirect('/stu/login/')
    if request.method == 'POST':
        tk = request.COOKIES.get('ticket')
        name = Student.objects.get(s_ticket=tk).s_name
        id = request.GET.get('id')
        size = request.POST.get('level')
        num = request.POST.get('num')
        na = sweaters.objects.get(id=id)
        ma = sweater.objects.get(id=na.ss_id).s_id
        stu = sweater.objects.filter(s_id=ma)
        stus = women.objects.all()
        zhu = Student.objects.get(s_name=name).id
        ji = StudentInfo.objects.create(si_size = size,si_name = na.sws_name,si_pic = na.sws_pic,si_num =num,ss_id =zhu,si_img = na.sws_img,si_sh = id )
        ji.save()
        lala = Student.objects.get(s_name=name).studentinfo_set.all()
        all = lala.count()

        sum = 0
        for st in lala:
            sum += st.si_pic
        stu = {'stu': stus, 'name': name, 'sum': sum, 'all': all, 'stus': stu, 'na': na}
        return render(request, 'new/single.html', stu)
def change(request):
    if request.method == 'GET':
        tk = request.COOKIES.get('ticket')
        if tk :
            name = Student.objects.get(s_ticket=tk).s_name
            stus = women.objects.all()
            id = request.GET.get('id')
            ki = StudentInfo.objects.get(id=id).si_sh
            na = sweaters.objects.get(id = ki)
            ma = sweater.objects.get(id = na.ss_id).s_id
            stu =sweater.objects.filter(s_id = ma)

            lala = Student.objects.get(s_name=name).studentinfo_set.all()
            all = lala.count()

            sum = 0
            for st in lala:
                sum += st.si_pic
            stu = {'stu': stus, 'name': name,'sum':sum,'all':all ,'stus':stu,'na':na}
            return render(request, 'new/single_change.html', stu)
        return HttpResponseRedirect('/stu/login/')
    if request.method == 'POST':
        # tk = request.COOKIES.get('ticket')
        # name = Student.objects.get(s_ticket=tk).s_name
        id = request.GET.get('id')
        size = request.POST.get('level')
        num = request.POST.get('num')
        # na = sweaters.objects.get(id=id)
        # ma = sweater.objects.get(id=na.ss_id).s_id
        # stu = sweater.objects.filter(s_id=ma)
        # stus = women.objects.all()
        # zhu = Student.objects.get(s_name=name).id
        # ji = StudentInfo.objects.create(si_size=size, si_name=na.sws_name, si_pic=na.sws_pic, si_num=num, ss_id=zhu,
        #                                 si_img=na.sws_img)
        ji = StudentInfo.objects.get(id = id)
        ji.si_size = size
        ji.si_num = num
        ji.save()
        # lala = Student.objects.get(s_name=name).studentinfo_set.all()
        # all = lala.count()

        # sum = 0
        # for st in lala:
        #     sum += st.si_pic
        # stu = {'stu': stus, 'name': name, 'sum': sum, 'all': all, 'stus': stu, 'na': na}
        return HttpResponseRedirect('/comm/car/')
def add(request):
    if request.method == 'GET':
        tk = request.COOKIES.get('ticket')
        if tk:
            id = Student.objects.get(s_ticket=tk).id
            lal =Student.objects.get(s_ticket=tk).studentinfo_set.all()
            for st in lal:
                ja = StudentShop.objects.create(sss_id = id,sis_pic =st.si_pic,sis_name = st.si_name,sis_num =st.si_num,sis_img =st.si_img,sis_size = st.si_size,sis_zh = '未处理',sis_sh=st.si_sh)
                ja.save()
            return HttpResponseRedirect('/comm/car/')