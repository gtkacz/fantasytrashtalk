from django.urls import path
from django.conf.urls import url
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    # path('accounts/login/', views.login),
    path('<str:username>/bids/', views.userbids),
    path('player/<str:playername>/', views.playerview),
    path('sortby=<str:sortvalue>/', views.sortby),
    # url(r'^login/$', views.login, name='login'),
]
