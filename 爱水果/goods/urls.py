from django.conf.urls import url


from goods import views
urlpatterns = [
    #商品列表
    url(r'^pro_list/', views.pro_list, name='pro_list'),

    url(r'^goods_del/', views.goods_del, name='goods_del'),
    #商品详情展示
    url(r'^pro_detail/', views.pro_detail, name='pro_detail'),
    url(r'^show/', views.show, name='show'),

    #商品回收站
    url(r'^pro_bin/', views.pro_bin, name='pro_bin'),
    url(r'^to_del/', views.to_del, name='to_del'),

    #分类展示
    url(r'^fen_list/', views.fen_list, name='fen_list'),
    url(r'^fen_detail/', views.fen_detail, name='fen_detail'),
    url(r'^to_show/', views.to_show, name='to_show'),
    url(r'^show_all/', views.show_all, name='show_all'),


]