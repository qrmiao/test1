from django.conf.urls import url
from rest_framework.routers import SimpleRouter

from commodity import views
router = SimpleRouter()
router.register(r'^show', views.Show)
router.register(r'^shop', views.Shop)
urlpatterns = [
    # url(r'^regist/', views.regist),
    # url(r'^login/', views.login),
    # url(r'^logout/', views.logout),
    url(r'^product/', views.product),
    url(r'^index/', views.index),
    # url(r'^indexin/(?P<name>.+)/', views.indexin , name='lala'),
    url(r'^del/', views.dell),
    url(r'^single/', views.single),
    url(r'^change/', views.change),
    url(r'^add/', views.add),
    url(r'^car/', views.car),

]
urlpatterns += router.urls