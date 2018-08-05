

# Create your models here.
from django.db import models
# 购物车模型
from goods.models import GoodsInfo
from user.models import UserInfo


class CartInfo(models.Model):
    # 外键用户
    user=models.ForeignKey(UserInfo)
    # 外键商品
    goods=models.ForeignKey(GoodsInfo)
    # 购买的数量
    count=models.IntegerField()
    class Meta:
          db_table = 'cartinfo'