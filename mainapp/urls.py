from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name="index"),
    path('contacto/', views.formularioContacto, name='contacto'),
    path('items/ak/', views.ak, name = 'ak'),
    path('items/awp/', views.awp1, name = 'awp'),
    path('items/m4/', views.m4, name = 'm4'),
    path('login/', views.logeo, name='login'),
    path('registro/', views.registro, name='registro'),
    path('logout/', views.deslogeo, name='deslogeo'),
    path('unloged/', views.unloged, name='unloged'),
    path('carrito/', views.carro, name='carrito'),
    path('agregar/<int:ak_id>/', views.agregar_producto, name="Add"),
    path('eliminar/<int:ak_id>/', views.eliminar_producto, name="Del"),
    path('restar/<int:ak_id>/', views.restar_producto, name="Sub"),
    path('limpiar/', views.limpiar_carrito, name="CLS"),
]