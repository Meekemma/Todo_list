from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name ="home"),
    path('delete_item/<str:pk>/', views.deleteItem, name ="delete_Item"),
    path('update_item/<str:pk>/', views.update, name = "update_item")
]