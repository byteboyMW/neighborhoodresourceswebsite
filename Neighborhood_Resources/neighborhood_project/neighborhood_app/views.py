from django.shortcuts import render
from django.views.generic import TemplateView

# Create your views here.

def index(request):
    return render(request, 'neighborhood_app/index.html')

class about(TemplateView):
    template_name = 'neighborhood_app/about.html'
    
class team(TemplateView):
    template_name = 'neighborhood_app/team.html'

class credit(TemplateView):
    template_name = 'neighborhood_app/credits.html'
    
class jobs(TemplateView):
    template_name = 'neighborhood_app/jobs.html'
    
class faq(TemplateView):
    template_name = 'neighborhood_app/faq.html'