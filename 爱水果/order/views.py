from django.http import JsonResponse
from django.shortcuts import render

# Create your views here.
from cart.models import CartInfo
from order.models import sales, OrderDetailInfo


def order_list(request):
    return render(request, 'back/order_list.html')


def order_detail(request):
    return render(request, 'back/order_detail.html')
def add(request):
    if request.method == 'POST':

        data = {}
        data['code'] = 1001

        user = request.unser
        if user and user.id:
            goods_id = request.POST.get('goods_id')
            # 获取购物车信息
            user_carts = CartInfo.objects.filter(user_id=user.id, goods_id=goods_id).first()
            # 如果用户选了商品
            if user_carts:
                user_carts.count += 1
                user_carts.save()
                data['c_num'] = user_carts.count
            else:
                # 如果用户没选商品，就创建
                CartInfo.objects.create(user=user,goods_id=goods_id,count=1)
                data['c_num'] = 1
                data['code'] = 200
                data['msg'] = '成功'
                return JsonResponse(data)
        return JsonResponse(data)






