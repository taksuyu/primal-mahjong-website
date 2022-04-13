from django.urls import path

from . import views

urlpatterns = [
    path('', views.index_view, name='index'),
    path('user/<str:username>', views.user_view, name='user'),
    path('logout/', views.logout_view, name='logout'),
]