"""mysite URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from django.urls import path, include
from django.views.generic.base import TemplateView
from . import views
from django.conf.urls.static import static
from django.conf import settings

urlpatterns = [
    path('base/', TemplateView.as_view(template_name="base.html")),#TODO:make this '' for home page
    path('admin/', admin.site.urls),
    path('', include('blog.urls')), #TODO:set this to blog/ later to add projects, sites, recpies, etc.
    path('demo404', TemplateView.as_view(template_name="404.html")),
    path('demo500', TemplateView.as_view(template_name="500.html"))
]   + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) \
    + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)

handler400 = 'mysite.views.error_400'
handler403 = 'mysite.views.error_403'
handler404 = 'mysite.views.error_404'
handler500 = 'mysite.views.error_500'
