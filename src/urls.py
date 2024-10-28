from django.urls import path
from . import views

urlpatterns = [
    path('', views.index, name='home'),
    path('informasi_pribadi/', views.informasi_pribadi, name='informasi_pribadi'),
    path('pendidikan/', views.pendidikan, name='pendidikan'),
    path('keterampilan/', views.keterampilan, name='keterampilan'),
    path('kontak/', views.kontak, name='kontak'),
]
