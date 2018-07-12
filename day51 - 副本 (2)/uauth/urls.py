from django.conf.urls import url
from django.contrib.auth.decorators import login_required

from uauth import views
urlpatterns = [
    # url(r'^regist/', views.regist),
    # url(r'^login/', views.login),
    # url(r'^logout/', views.logout),
    url(r'^index/', login_required(views.index)),
    url(r'^dj_login/',views.djlogin),
    url(r'^dj_regist/', login_required(views.djregist)),
    url(r'^dj_logout/', login_required(views.djlogout)),
]