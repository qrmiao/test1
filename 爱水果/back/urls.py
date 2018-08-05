from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from back import views
urlpatterns = [
    # url(r'^regist/', views.regist),
    # url(r'^login/', views.login),
    # url(r'^logout/', views.logout),
    url(r'^index/', views.index, name='index'),
    url(r'^dj_login', views.dj_login, name='dj_login'),
    url(r'^dj_regist', views.dj_regist, name='dj_regist'),
    url(r'^dj_logout', views.dj_logout, name='dj_logout'),
    url(r'^user_list/', views.user_list, name='user_list'),
    url(r'^user_detail/', views.user_detail, name='user_detail'),


]