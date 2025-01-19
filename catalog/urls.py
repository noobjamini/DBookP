from django.urls import path
from catalog import views

urlpatterns = [
    path('', views.index, name='index'),
    path('apply/', views.apply_form, name='apply_form'),
    path('survey-complete/', views.survey_complete, name='survey_complete'),
    path('quswoalsrlawnstj/', views.application_list, name='application_list'),
]