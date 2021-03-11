from django.urls import path
from .import views

urlpatterns = [
    path('', views.home, name='home_url'),
    path('prod/', views.prod_list, name='prod_list_url'),
    path('prod/<str:slug>/', views.prod_detail, name='prod_detail_url'),
]