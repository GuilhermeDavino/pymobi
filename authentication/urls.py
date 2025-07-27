from django.urls import path 
from . import views
urlpatterns = [
    path('', views.auth, name='auth'),
    path('cadastro/', views.cadastro, name='cadastro'),
    path('logar/', views.logar, name='logar'),

]
