from django.views.generic import ListView, DetailView
from . models import Article
# Create your views here.

class ArticlelsView(ListView):
	model = Article
	template_name = 'home.html'


class DetailedView(DetailView):
	model = Article
	template_name = 'detail.html'
	context_object_name = 'article'