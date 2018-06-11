"""task1 URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.0/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path,re_path
from django.conf.urls import include
from django.conf.urls.static import static
from django.contrib import admin
from django.contrib.staticfiles.urls import staticfiles_urlpatterns
from django.conf import settings
from myapp import views
admin.autodiscover()

urlpatterns = [
    path('oauth/',include('social_django.urls', namespace = 'social')),
    path('login/', views.login1),
    path('register/',views.registers),
    re_path(r'^home/$',views.home),
    re_path(r'^home/(?P<username>\w+|)/$',views.home),
    path('logout/',views.logout_),
    path('post/',views.post),
    re_path(r'like/$',views.Like),
    re_path(r'dislik/$',views.Dislike),
    re_path(r'^comment/(?P<post_id>\w+)/$',views.comment),
    path('',views.re),

]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


urlpatterns += staticfiles_urlpatterns()
