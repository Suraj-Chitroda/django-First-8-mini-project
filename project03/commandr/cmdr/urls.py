
from django.urls import path
from . import views

urlpatterns = [
    path('',views.Homepageview.as_view()),
]
