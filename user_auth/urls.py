from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='user_index'),
    path('login', views.login, name="login"),    
    path('logout', views.logout, name="logout"),    
    path('status', views.status, name="status"),   
]
