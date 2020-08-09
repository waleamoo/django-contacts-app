"""contacts URL Configuration

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
from django.urls import path, include
from django.conf import settings #import for displaying image on page
from django.conf.urls.static import static #import for displaying image on page

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', include('app.urls')), #sets the home url path
    path('', include('django.contrib.auth.urls')), #sets the authentication url path
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT) #import for displaying image on page

# customizing admin texts 
admin.site.site_header = "Contacts"
admin.site.index_title = "Welcome to contacts"
admin.site.site_title = "Control Panel"