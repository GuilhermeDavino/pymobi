from django.urls import include, path 
from . import views
urlpatterns = [
    path('', views.auth, name='auth'),

]
