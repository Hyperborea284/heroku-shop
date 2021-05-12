from django.views.generic import TemplateView


class HomePageView(TemplateView):
    template_name = "home.html"


class AboutPageView(TemplateView):
    template_name = "about.html"


class Profile(TemplateView):
    template_name = "profile.html"


class Termos(TemplateView):
    template_name = "termos-de-uso.html"

