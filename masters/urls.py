from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='master_index'),
    path('parties', views.parties, name="parties")
]
