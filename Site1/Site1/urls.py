"""
URL configuration for Site1 project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
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
from django.urls import path
from . import veiws

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', veiws.index, name='index'),
    #pipe
    #path('about', veiws.about, name='about'),
    path('analyze', veiws.analyze, name='analyze'),

    #path('capfirst', veiws.capfirst, name='capfirst'),
    #path ('newlineremove', veiws.newlineremove, name='newlineremove'),
    #path ('spaceremove', veiws.spaceremove, name= 'spaceremove'),
    #path ('charcount', veiws.charcount, name='charcount'),

    #ex1
    #path('nav',veiws.nav,name='nav')


]
