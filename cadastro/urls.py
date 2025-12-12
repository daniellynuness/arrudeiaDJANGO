from django.urls import path
from . import views

urlpatterns = [
    path('', views.cadastro, name='cadastro'),
    path('login/', views.login_view, name='login'),
    path('logout/', views.logout_view, name='logout'),
    path('index/', views.index, name='index'),
    path('eventos/', views.eventos, name='eventos'),
    path('faq/', views.faq, name='faq'),
    path('feed/', views.feed, name='feed'),
    path('guias/', views.guias, name='guias'),
    path('home_off/', views.home_off, name='home_off'),
    path('parcerias/', views.parcerias, name='parcerias'),
]