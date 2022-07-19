from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='po_index'),
    path('listall', views.listall, name='po_all'),
]
