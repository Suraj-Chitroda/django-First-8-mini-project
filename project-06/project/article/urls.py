from django.urls import path
from . import views

urlpatterns = [
    path('', views.ArticlelsView.as_view(), name='home'),
    path('article/no=<int:pk>', views.DetailedView.as_view(), name='details'),
    path('article/new/', views.CreateArticle.as_view(), name='create_article'),
    path('article/no=<int:pk>/edit',
         views.UpdateArticle.as_view(), name="update_article"),
    path('article/no=<int:pk>/delete',
         views.DeleteArticle.as_view(), name="delete_article")
]
