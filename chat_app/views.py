from django.shortcuts import render
from django.views.generic import TemplateView


class HomeView(TemplateView):

    template_name = "chat_app/home.html" 




