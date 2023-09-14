from django.shortcuts import render
from django.views import generic
from . import models


class HomePage(generic.TemplateView):
    """
    Display the home page
    """
    template_name = 'main/index.html'


class AboutPage(generic.TemplateView):
    """
    Display the about page
    """
    template_name = 'main/about.html'


class TeamPage(generic.ListView):
    queryset = models.Employee.objects.order_by('last_name')
    template_name = 'main/team.html'


class ContactPage(generic.TemplateView):
    template_name = 'main/contact.html'


class CareersPage(generic.TemplateView):
    template_name = 'main/careers.html'
