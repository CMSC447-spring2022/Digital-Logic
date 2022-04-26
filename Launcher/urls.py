from django.urls import path

from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('add/', views.add, name='add'),
    path('destroy_all/', views.destroy_all, name='destroy_all'),
]