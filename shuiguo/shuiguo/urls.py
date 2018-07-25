"""shuiguo URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.11/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  url(r'^$', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  url(r'^$', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.conf.urls import url, include
    2. Add a URL to urlpatterns:  url(r'^blog/', include('blog.urls'))
"""
from django.conf.urls import url,include
from django.contrib import admin
from django.contrib.staticfiles.urls import static

urlpatterns = [
    url(r'^admin/', admin.site.urls),
    url(r'^tinymce/', include('tinymce.urls')),
    url(r'^back/', include('back.urls', namespace='back')),
    url(r'^user/', include('user.urls', namespace='user')),
    # url(r'^app/', include('app.urls', namespace='app')),
]
from shuiguo import settings
### 将上传图片的文件夹静态化
urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)