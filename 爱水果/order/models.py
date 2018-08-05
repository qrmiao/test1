from django.db import models

# Create your models here.
# 订单表模型
class OrderInfo(models.Model):
    oid = models.CharField(max_length=20, primary_key=True)
    user = models.ForeignKey('user.UserInfo')
    odate = models.DateTimeField(u'购买日期',auto_now=True)
    # 付款属性
    oIsPay = models.BooleanField(u'是否付款',default=False)
    # 总价
    ototal = models.DecimalField(u'总价',max_digits=6, decimal_places=2)
    oaddress = models.CharField(u'收货地址',max_length=150)

    # def __str__(self):
    #     if self.oIsPay==True:
    #         return self.oaddress
    #     else :
    #         return '未付款'

    # 修改后台显示名字
    class Meta:
        db_table = 'orderinfo'

# 订单详表
class OrderDetailInfo(models.Model):

    goods = models.ForeignKey('goods.GoodsInfo')
    order = models.ForeignKey(OrderInfo)
    # 总价
    price = models.DecimalField(u'价钱',max_digits=5, decimal_places=2)
    # 数量
    count = models.IntegerField(u'数量')
    # 统计销量是否统计进去
    isTrue=models.BooleanField(default=False)

    # 修改后台显示名字
    class Meta:
        db_table = 'orderdetailinfo'
#销量统计
class sales(models.Model):
    # 水果名称
    goods = models.ForeignKey('goods.GoodsInfo')
    # 销量
    count=models.IntegerField(u'销量')
    # 销售额
    totalprice=models.DecimalField(u'销售额',max_digits=5, decimal_places=2)
 # 修改后台显示名字
    class Meta:
        db_table = 'sales'