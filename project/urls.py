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
    path('board', views.BoardListView.as_view(), name='board'),
    path('board/<int:pk>', views.BoardDetail.as_view(), name='board-detail'),
    path('accounts/', include('django.contrib.auth.urls')),
    path('accounts/signup', views.CreateUserView.as_view(), name='signup'),
    path('accounts/signup/signup_done', views.RegisteredView.as_view(), name='signup_done'),
    path('board/writepost', views.WritePostView.as_view(), name='writepost'),
    path('board/<int:pk>/commentremove', views.comment_remove, name='comment_remove'),
    path('board/<int:pk>/boardremove', views.board_remove, name='board_remove'),
    path('board/<int:pk>/editboard', views.BoardUpdate.as_view(), name='board_update_form'),
    path('board/<int:pk>/<int:id>editcomment', views.CommentUpdate.as_view(), name='comment_update_form'),
    path('board/search', views.BoardSearchListView.as_view(), name='board_search_list_view'),
]