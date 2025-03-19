from django.contrib import admin
from django.urls import path
from . import views

urlpatterns = [
    path('', views.home, name='home'),
    path('production/', views.production, name='production'),
    path('dovegel/', views.dovegel, name='dovegel'),
    path('inventory/', views.inventory, name='inventory'),
    path('products/', views.products, name='products'),
    path('rawmaterials/', views.rawmaterials, name='rawmaterials'),
]