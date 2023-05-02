from django.urls import path
from .views import HomePage, AboutPage, OurServices, ContactsPage

urlpatterns = [
    path("", HomePage.as_view(), name="Home"),
    path("about/", AboutPage.as_view(), name="About"),
    path("services/", OurServices.as_view(), name="Services"),
    path("contacts/", ContactsPage.as_view(), name="Contacts"),
]
