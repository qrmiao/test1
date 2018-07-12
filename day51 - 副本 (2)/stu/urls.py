from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from stu import views

from rest_framework.routers import SimpleRouter

router = SimpleRouter()
router.register(r'^student', views.StudentEdit)

urlpatterns = [
    # url(r'^aStuPage/', login_required(views.aStuPage)),
    url(r'^regist', views.regist),
    url(r'^login', views.login),
    url(r'^product', views.product),
    url(r'^lalal', views.lalal),
    url(r'^del', views.ddel),
    url(r'^main_in', views.main_in),


    url(r'^test', login_required(views.test)),
    url(r'^index', views.index),
    url(r'^top/', views.top),
    url(r'^bottom/', views.bottom),
    url(r'^swich/', views.swich),
    url(r'^left/', views.left),
    url(r'^main/', views.main),
    url(r'^add/', views.add),
    url(r'^main_list/', views.main_list),
    url(r'^main_menu/', views.main_menu),
    url(r'^main_add/', views.main_add),
    url(r'^main_change/', views.main_change),
    url(r'^main_menu_del/', views.main_menu_del),
    url(r'^main_menu_add/', views.main_menu_add),
    url(r'^main_menu_next/', views.main_menu_next),
    url(r'^main_menu_last/', views.main_menu_last),
    url(r'^main_menu_change/', views.main_menu_change),
    url(r'^main_message/', views.main_message),
    url(r'^message_info/', views.message_info),
    url(r'^message_replay/', views.message_replay),
    url(r'^message_del/', views.message_del),
    url(r'^message_ok/', views.message_ok),
    url(r'^test/', views.test),


    # url(r'^index/', login_required(views.index)),
    # url(r'^stuPage/', login_required(views.stuPage)),
    # url(r'^addstu/', login_required(views.addStu), name='add'),
    # url(r'^addstuInfo/(?P<stu_id>\d+)/', login_required(views.addStuInfo), name='addinfo')
]

urlpatterns += router.urls
