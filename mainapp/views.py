# mainapp/views.py
from django.shortcuts import render
from django.views.generic import TemplateView

class HomeView(TemplateView):
    template_name = 'mainapp/home.html'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context['title'] = 'Welcome to QuestDock'
        return context

def about(request):
    return render(request, 'mainapp/about.html', {'title': 'About Us'})