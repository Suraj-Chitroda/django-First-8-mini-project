from django.views.generic import TemplateView

class homeview(TemplateView):
	"""docstring for homeview"""

	template_name = 'index.html'

class aboutview(TemplateView):
	template_name = 'about.html'

class contactview(TemplateView):
	template_name = 'contact.html'
