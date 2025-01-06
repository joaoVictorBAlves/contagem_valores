from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='index'),
    path('registrar_valor/', views.registrar_valor, name='registrar_valor'),
]
