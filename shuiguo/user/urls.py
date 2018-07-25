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
    url(r'^info/', views.info, name='info'),
    url(r'^order/', views.order, name='order'),
    url(r'^cart/', views.cart, name='cart'),
    url(r'^site/', views.site, name='site'),
    url(r'^place/', views.place, name='place'),


]