from django.core.paginator import Paginator
from django.http import HttpResponseRedirect
from django.shortcuts import render

# Create your views here.
from django.urls import reverse

from goods.models import GoodsInfo, TypeInfo


# 商品列表信息
def pro_list(request):
    if request.method =='GET':
        page_id = request.GET.get('page_id', 1)
        data={}
        goods = GoodsInfo.objects.filter(isDelete=False)
        paginator = Paginator(goods, 4)
        page = paginator.page(int(page_id))
        data['goods'] = page
        return render(request, 'back/product_list.html',data)
def pro_detail(request):
    if request.method == 'GET':
        fen = TypeInfo.objects.filter(isDelete=False)
        return render(request, 'back/product_detail.html',{'fen':fen})
    if request.method == 'POST':
        name = request.POST.get('name')
        pic = request.POST.get('pic')
        wei = request.POST.get('wei')
        kucui = request.POST.get('kucui')
        jianjie = request.POST.get('jianjie')
        fenlei = request.POST.get('fenlei')
        isjin = request.POST.get('isjin',0)
        isre = request.POST.get('isre',0)
        isxin = request.POST.get('isxin',0)
        img = request.FILES.get('img')
        xiang = request.POST.get('xiang')
        stu = GoodsInfo.objects.create(gtitle=name,gpic=img,gprice=pic,isDelete=0,gunit=wei,gjianjie=jianjie,gkucun=kucui,gcontent=xiang,gtype_id=fenlei,isjin=isjin,isre=isre,isxin=isxin)
        return HttpResponseRedirect(reverse('goods:pro_list'))
5

#商品回收站列表
def pro_bin(request):
    if request.method == 'GET':
        page_id = request.GET.get('page_id', 1)
        data = {}
        goods = GoodsInfo.objects.filter(isDelete=True)
        paginator = Paginator(goods, 4)
        page = paginator.page(int(page_id))
        data['goods'] = page


        return render(request, 'back/recycle_bin.html',data)

def goods_del(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        fid  = request.GET.get('fid')
        if id:
            goods = GoodsInfo.objects.get(id=id)
            goods.isDelete = True
            goods.save()
            return HttpResponseRedirect(reverse('goods:pro_list'))
        if fid:
            goods = TypeInfo.objects.get(id=fid)
            goods.isDelete = True
            goods.save()
            return HttpResponseRedirect(reverse('goods:fen_list'))


def to_del(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        GoodsInfo.objects.get(id =id).delete()
        return HttpResponseRedirect(reverse('goods:pro_bin'))
def show(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        good = GoodsInfo.objects.get(id =id)
        fen = TypeInfo.objects.filter(isDelete=False)
        return render(request, 'back/product_show.html', {'good':good,'fen':fen})
    if request.method =='POST':
        id =request.GET.get('id')
        good = GoodsInfo.objects.get(id=id)
        name = request.POST.get('name')
        pic = request.POST.get('pic')
        wei = request.POST.get('wei')
        kucui = request.POST.get('kucui')
        jianjie = request.POST.get('jianjie')
        fenlei = request.POST.get('fenlei')
        isjin = request.POST.get('isjin', 0)
        isre = request.POST.get('isre', 0)
        isxin = request.POST.get('isxin', 0)
        img = request.FILES.get('img')
        xiang = request.POST.get('xiang')
        good.gtitle = name
        good.gpic = img
        good.gprice = pic
        good.googunit = wei
        good.gjianjie = jianjie
        good.gkucun = kucui
        good.gcontent = xiang
        good.gtype_id = fenlei
        good.isjin = isjin
        good.isre = isre
        good.isxin = isxin
        good.save()
        return HttpResponseRedirect(reverse('goods:pro_list'))

def fen_list(request):
    if request.method =='GET':
        page_id = request.GET.get('page_id', 1)
        data={}
        goods = TypeInfo.objects.filter(isDelete=False)
        paginator = Paginator(goods, 4)
        page = paginator.page(int(page_id))
        data['goods'] = page
        return render(request, 'back/fen_list.html',data)
def fen_detail(request):
    if request.method =='GET':
        fen = TypeInfo.objects.filter(isDelete=False)
        return render(request, 'back/fen_detail.html', {'fen': fen})
    if request.method == 'POST':
        name = request.POST.get('name')
        pic = request.FILES.get('pic')
        TypeInfo.objects.create(ttitle=name, pic=pic, )
        return HttpResponseRedirect(reverse('goods:fen_list'))
def to_show(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        good = TypeInfo.objects.get(id =id)

        return render(request, 'back/fen_show.html', {'good':good,})
    if request.method == 'POST':
        id = request.GET.get('id')
        good = TypeInfo.objects.get(id =id)
        name = request.POST.get('name')
        pic = request.FILES.get('pic')
        good.ttitle = name
        good.pic = pic
        good.save()
        return HttpResponseRedirect(reverse('goods:fen_list'))

def show_all(request):
    if request.method == 'GET':
        id = request.GET.get('id')
        good = TypeInfo.objects.get(id =id).goodsinfo_set.all()
        page_id = request.GET.get('page_id', 1)
        data = {}
        goods = good.filter(isDelete=False)
        paginator = Paginator(goods, 4)
        page = paginator.page(int(page_id))
        data['goods'] = page
        return render(request, 'back/product_list.html', data)

