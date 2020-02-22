"""notes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.0/topics/http/urls/
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
from django.urls import include, path
# for static files like (images, css ---)
from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    path('admin/', admin.site.urls),
    # include our own urls.py
    path('', include('home.urls', namespace='home')),
    path('notes/', include('notes_app.urls', namespace='notes')),
    path('accounts/', include('accounts.urls', namespace='accounts')),

    path('ckeditor/', include('ckeditor_uploader.urls')),
    
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)


# Admin panel customazation
admin.site.site_header = 'Notize Admin Panel'
admin.site.site_title = 'Notize'
admin.site.site_index_header = 'Welcome To Notize Admin Panel'