from django.contrib import admin
from django.urls import path, include, re_path
from core import settings
from django.conf.urls.static import static
from django.views.static import serve

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')),
    re_path(r'^media/(?P<path>.*)$', serve,{'document_root': settings.MEDIA_ROOT}), 
    re_path(r'^static/(?P<path>.*)$', serve,{'document_root': settings.STATIC_ROOT}), 
] 

admin.site.site_header = "Y-Portfolio Admin"
admin.site.site_title = "Your Portfolio Admin Portal"
admin.site.index_title = "Welcome to Y-Portfolio Admin"