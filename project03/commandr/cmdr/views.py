from django.views.generic import ListView

from .models import cmdr

class Homepageview(ListView):

    template_name = 'home.html'
    model = cmdr
