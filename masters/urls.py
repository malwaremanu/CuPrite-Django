from django.urls import path, include
from rest_framework import routers
from . import views

# router = routers.DefaultRouter()

# router.register('api_party', views.partyViewSet)

urlpatterns = [
    path('', views.index, name='master_index'),
    # path('', include(router.urls)),    
    path('parties/<str:pk>', views.party_detail),
    path('parties', views.party_detail),
]
