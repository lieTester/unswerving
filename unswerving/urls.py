"""unswerving URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.0/topics/http/urls/
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
from unswerving.settings import MEDIA_ROOT
from django.contrib import admin
from django.conf import settings
from django.urls import include, path
from django.conf.urls.static import static, serve
from django.urls.conf import re_path


urlpatterns = [

    ##### user related path##########################
    # path('', views.home_view),
    path('admin_django/', admin.site.urls),
    path('admin_portal/', include('admin_portal.urls')),
    path('', include('lander_portal.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,
            {'document_root': settings.MEDIA_ROOT}),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL,
                          document_root=settings.MEDIA_ROOT)
