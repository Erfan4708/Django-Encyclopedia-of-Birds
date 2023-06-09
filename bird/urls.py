from django.urls import path

from .views import BirdList, BirdDeleteView, KingdomList

urlpatterns = [
    path('', BirdList.as_view(), name='bird_list'),
    path('/delete/<int:pk>/', BirdDeleteView.as_view(), name='bird_delete'),
    path('/domain/<str:domain_name>/kingdoms/', KingdomList.as_view(), name='kingdom_list'),

]
