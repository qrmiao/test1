from user import views
from django.conf.urls import url
urlpatterns = [
    # url(r'^regist/', views.regist),
    # url(r'^login/', views.login),
    # url(r'^logout/', views.logout),
    url(r'^index/', views.index, name='index'),
    url(r'^login', views.login, name='login'),
    url(r'^regist', views.regist, name='regist'),
    url(r'^logout', views.logout, name='logout'),


]