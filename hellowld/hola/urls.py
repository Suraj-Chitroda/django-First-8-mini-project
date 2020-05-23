
from django.urls import path
from . import views

urlpatterns = [
    path('', views.india, name='home' ),
    path('spanish/', views.spain, name='home' ),
]
