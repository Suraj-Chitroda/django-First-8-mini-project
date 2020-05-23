from django.urls import path

from . import views

urlpatterns = [
    path('', views.homeview.as_view(), name='home'),
    path('about/', views.aboutview.as_view(), name='about'),
    path('contact/', views.contactview.as_view(), name='contact'),
]
