from django.conf.urls import url


from order import views
urlpatterns = [
    #订单详情展示
    url(r'^order_detail/', views.order_detail, name='order_detail'),
    #订单列表
    url(r'^order_list/', views.order_list, name='order_list'),
    url(r'^add/', views.add, name='add'),
    # url(r'^sub/', views.sub, name='sub'),




]