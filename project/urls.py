"""project URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.1/topics/http/urls/
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
from portfolio import views
from portfolio.views import BoardDetail
from django.views.generic.dates import ArchiveIndexView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.index, name='index'),
    path('board', views.board, name='board'),
    path(r'^board/(?P<pk>\d+)/$', views.BoardDetail.as_view(), name='board-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path(r'^accounts/signup$', views.CreateUserView.as_view(), name='signup'),
    path(r'^accounts/signup/signup_done', views.RegisteredView.as_view(), name='signup_done'),
    path(r'^board/writepost$', views.WritePostView.as_view(), name='writepost'),
]
