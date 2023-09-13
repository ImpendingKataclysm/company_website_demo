from django.shortcuts import render
from django.views import generic


class HomePage(generic.TemplateView):
    template_name = 'main/index.html'


class AboutPage(generic.TemplateView):
    template_name = 'main/about.html'


class TeamPage(generic.TemplateView):
    template_name = 'main/team.html'


class ContactPage(generic.TemplateView):
    template_name = 'main/contact.html'


class CareersPage(generic.TemplateView):
    template_name = 'main/careers.html'
