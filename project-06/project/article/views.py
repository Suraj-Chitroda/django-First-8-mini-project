from django.views.generic import ListView, DetailView
from django.views.generic.edit import CreateView, UpdateView, DeleteView
from django.urls import reverse_lazy
from . models import Article
# Create your views here.


class ArticlelsView(ListView):
    model = Article
    template_name = 'home.html'


class DetailedView(DetailView):
    model = Article
    template_name = 'detail.html'
    context_object_name = 'article'


class CreateArticle(CreateView):
    model = Article
    template_name = 'create.html'
    fields = '__all__'


class UpdateArticle(UpdateView):
    model = Article
    template_name = 'update.html'
    fields = ['title', 'text']


class DeleteArticle(DeleteView):
    model = Article
    template_name = 'delete.html'
    context_object_name = 'del'
    success_url = reverse_lazy('home')
