from django.urls import path

from . import views

#URLConf - Every App has one 
urlpatterns = [
    path('', views.index, name = 'main'),
    path('keys/', views.keys, name ='keys'),
    path('encrypted/', views.encrypted, name = 'encrypted'),
]