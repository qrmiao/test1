

# Create your models here.
from django.db import models
# 购物车模型
class CartInfo(models.Model):
    # 外键用户
    user=models.ForeignKey('user.UserInfo')
    # 外键商品
    goods=models.ForeignKey('goods.GoodsInfo')
    # 购买的数量
    count=models.IntegerField()
