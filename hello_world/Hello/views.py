from django.views.generic import TemplateView


class HomePage(TemplateView):
    template_name = "Home.html"


class AboutPage(TemplateView):
    template_name = "About.html"


class OurServices(TemplateView):
    template_name = "Services.html"


class ContactsPage(TemplateView):
    template_name = "Contacts.html"
