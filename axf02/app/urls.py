from django.conf.urls import url,include
from app import views
urlpatterns = [

    url(r'^home', views.home, name='home'),
    url(r'^mine', views.mine, name='mine'),
    url(r'^market/$', views.market, name='market'),
    url(r'^market/(?P<typeid>\d+)/(?P<cid>\d+)/(?P<sid>\d+)/', views.marketparams, name='marketparams'),
    url(r'^addgoods', views.add_goods, name='addgoods'),
    url(r'^subgoods', views.sub_goods, name='subgoods'),
    url(r'^cart', views.cart, name='cart'),

]
