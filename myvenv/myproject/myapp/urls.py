from django.contrib import admin
from django.urls import path
from . import views
from .views import rawmaterials_view

urlpatterns = [
    path('', views.home, name='home'),
    path('production/', views.production, name='production'),
    path('dovegel/', views.dovegel, name='dovegel'),
    path('inventory/', views.inventory, name='inventory'),
    path('products/', views.products, name='products'),
    path('rawmaterials/', views.rawmaterials, name='rawmaterials'),
    path('add_powder/', views.add_powder, name='add_powder'),
    path('add_container/', views.add_container, name='add_container'),
    path('add_cap/', views.add_cap, name='add_cap'),
    path("rawmaterials/", rawmaterials_view, name="rawmaterials"),
]
