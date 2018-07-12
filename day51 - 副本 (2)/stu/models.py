from django.db import models


class Student(models.Model):

    s_name = models.CharField(max_length=10)
    s_password = models.CharField(max_length=255)
    s_operate_time = models.DateField(null=True)

    s_emil = models.CharField(max_length=11)

    s_ticket = models.CharField(max_length=30, null=True)

    class Meta:
        db_table = 'student'


class StudentInfo(models.Model):


    si_name =  models.CharField(max_length=10)
    si_num = models.IntegerField()
    si_sh = models.IntegerField()
    si_img = models.ImageField(upload_to='upload', null=True)
    si_pic = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    si_size = models.CharField(max_length=100)
    ss = models.ForeignKey('student')

    class Meta:
        db_table = 'Student_info'

class StudentShop(models.Model):


    sis_name =  models.CharField(max_length=10)
    sis_num = models.IntegerField()
    sis_sh = models.IntegerField()
    sis_img = models.ImageField(upload_to='upload', null=True)
    sis_pic = models.DecimalField(max_digits=10, decimal_places=3, null=True)
    sis_size = models.CharField(max_length=100)
    sis_zh = models.CharField(max_length=255)
    sss = models.ForeignKey('student')

    class Meta:
        db_table = 'Student_shop'
class Visit(models.Model):

    v_url = models.CharField(max_length=30)
    v_times = models.IntegerField()

    class Meta:
        db_table = 'day7_visit'


class Promission(models.Model):
    p_name = models.CharField(max_length=30)

    class Meta:
        db_table = 'Promission'

class My_Role(models.Model):
    my_name = models.CharField(max_length=30)
    my_p=models.ManyToManyField(Promission)
    class Meta:
        db_table = 'My_Role'


class MyUser(models.Model):

    my_name = models.CharField(max_length=30)
    my=models.ForeignKey(My_Role)

    class Meta:
        db_table = 'MyUser'

