from django.urls import path
from . import views

urlpatterns = [
    path('', views.index_exp, name='index'),
    path('complete/<int:td_id>', views.complete, name='complete'),
    path('delete', views.delete, name='del')
]
