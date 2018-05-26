"""gandi URL Configuration

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
from django.urls import path

from django.contrib.auth.views import login, logout
from index.views import home
from Domains.views import *
#from Domains.views import DNDetail
#from Domains.views import DNQuery
#from Domains.views import jDNQuery
#from Domains.views import DNCreate
#from Domains.views import preDNCreate
from Contacts.views import CTDetail

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/login/', login, name='login' ),
    path('accounts/logout/', logout, name='logout' ),
    path('accounts/profile/', home),
    path('index/', home ),
    path('DNDetail/<str:fqdn>', DNDetail ),
    path('CTDetail/<str:ctid>', CTDetail ),
    path('DNQuery/<str:fqdn>', DNQuery ),
    path('jDNQuery/<str:fqdn>', jDNQuery ),
    path('DNCreate/', DNCreate ),
    path('preDNCreate/<str:fqdn>', preDNCreate ),
]
