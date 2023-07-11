"""chatbot_tutorial URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/1.10/topics/http/urls/
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
from django.conf.urls import url
from django.contrib import admin
from .views import chat,user_calls
from .views import signup, user_login, user_logout
from django.contrib.auth import views as auth_views

urlpatterns = [
	url(r'^chat/$', chat, name='chat'),
    url(r'^admin/', admin.site.urls),
    url(r'^user_calls/$', user_calls, name='user_calls'),
    url(r'^signup/$', signup, name='signup'),
    url(r'^login/$', user_login, name='login'),
    url(r'^logout/$', user_logout, name='logout'),
    
]
