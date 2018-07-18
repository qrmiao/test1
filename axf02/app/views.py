from django.http import HttpResponseRedirect, JsonResponse
from django.shortcuts import render

# Create your views here.
from app.models import MainShow, MainWheel, MainNav, MainMustBuy, MainShop, Goods, FoodType, CartModel
from django.core.urlresolvers import reverse

def home(request):
    if request.method == 'GET':
        mainShow = MainShow.objects.all()
        banner = MainWheel.objects.all()
        nav = MainNav.objects.all()
        mustBuy = MainMustBuy.objects.all()
        shops = MainShop.objects.all()
        return render(request, 'home/home.html',{'mainshow': mainShow,'banner':banner,'nav':nav,'mustBuy':mustBuy,
                                                 'shop1':shops[0],
                                                 'shop2':shops[1:3],
                                                 'shop3':shops[3:7],
                                                 'shop4':shops[7:11:]})
def mine(request):
    if request.method == 'GET':
        return render(request, 'mine/mine.html')
def market(request):
    if request.method == 'GET':
        return HttpResponseRedirect(reverse('app:marketparams', kwargs={
            'typeid':104749,
            'cid':0,
            'sid':0

        }))
def marketparams(request,typeid,cid,sid):
    foodtype = FoodType.objects.all()

    a = FoodType.objects.filter(typeid =typeid).first().childtypenames
    if cid == '0':
        goods = Goods.objects.filter(categoryid=typeid)
    else:
        goods = Goods.objects.filter(categoryid=typeid,
                                           childcid=cid)
    if sid == '0':
        pass
    elif sid == '1':
        goods = goods.order_by('productnum')
    elif sid == '2':
        goods = goods.order_by('-price')
    elif sid == '3':
        goods = goods.order_by('price')
    child = [i.split(':') for i in a.split('#')]
    user = request.user
    if user.id:
        try:
            cart_goods = CartModel.objects.filter(user=user)
        except CartModel.DoesNotExist:
            cart_goods = []
    else:
        cart_goods = []
    goods_ids = []
    if len(cart_goods) > 0:
        for cart_good in cart_goods:
            goods_ids.append(cart_good.goods.id)
    data={
        'foodtype':foodtype,
       'goods':goods,
        'child':child,
        'cid':cid,
        'typeid':typeid,
        'goods_ids' : goods_ids,
        'cart_goods' : cart_goods
    }
    return render(request,'market/market.html',data)
def add_goods(request):

    if request.method == 'POST':

        data = {}
        data['code'] = 1001

        user = request.user
        if user and user.id:
            goods_id = request.POST.get('goods_id')
            # 获取购物车信息
            user_carts = CartModel.objects.filter(user=user, goods_id=goods_id).first()
            # 如果用户选了商品
            if user_carts:
                user_carts.c_num += 1
                user_carts.save()
                data['c_num'] = user_carts.c_num
            else:
                # 如果用户没选商品，就创建
                CartModel.objects.create(user=user,
                                         goods_id=goods_id,
                                         c_num=1)
                data['c_num'] = 1
                data['code'] = 200
                data['msg'] = '成功'
                return JsonResponse(data)
        return JsonResponse(data)
def sub_goods(request):

    if request.method == 'POST':
        data = {
            'code':'200',
            'msg': '请求成功'
        }
        user = request.user
        goods_id = request.POST.get('goods_id')

        if user and user.id:
            # 查看当前商品是否已经在购物中
            user_carts = CartModel.objects.filter(user=user,
                                                  goods_id=goods_id).first()
            # 如果存在，则减一
            if user_carts:
                # 如果商品的数量为1，则删除
                if user_carts.c_num == 1:
                    user_carts.delete()
                    data['c_num'] = 0
                else:
                    # 如果商品数量不为一，则减一
                    user_carts.c_num -= 1
                    user_carts.save()
                    data['c_num'] = user_carts.c_num
        return JsonResponse(data)
def cart(request):

    if request.method == 'GET':
        data = {}
        user = request.user
        cart_goods = CartModel.objects.filter(user=user)
        data['cart_goods'] = cart_goods
        data['cart_sum'] = get_cart_sum(user)
        return render(request, 'cart/cart.html', data)


def get_cart_sum(user):
    cart_goods = CartModel.objects.filter(user=user)
    cart_sum = 0
    for cart_good in cart_goods:
        cart_sum += cart_good.goods.price * cart_good.c_num
    return cart_sum