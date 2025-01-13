from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('introduce/',views.introduce, name='introduce'),
    path('apply/', views.apply, name='apply'),
]