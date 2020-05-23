
from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlelsView.as_view(), name='home'),
    path('article/no=<int:pk>', views.DetailedView.as_view(), name='details'),
]
