from django.db import models


class women(models.Model):
    w_name = models.CharField(max_length=10)
    class Meta:
        db_table = 'women'

class sweater(models.Model):
    sw_name = models.CharField(max_length=10)
    s = models.ForeignKey('women')

    class Meta:
                db_table = 'sweater'
class sweaters(models.Model):
    sws_name = models.CharField(max_length=10)
    sws_pic = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    sws_img = models.ImageField(upload_to='upload', null=True)
    sws_img1 = models.ImageField(upload_to='upload', null=True)
    sws_img2 = models.ImageField(upload_to='upload', null=True)
    sws_introduction = models.CharField(max_length=2555)
    sws_size = models.IntegerField()
    sws_num = models.IntegerField()
    sws_operate_time = models.DateTimeField(auto_now_add=True)
    ss = models.ForeignKey('sweater')

    class Meta:
                db_table = 'sweaters'
class Img(models.Model):
    img = models.ImageField(upload_to='upload', null=True)
    class Meta:
        db_table = 'Img'