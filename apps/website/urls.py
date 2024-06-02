from django.urls import path
from . import views

app_name = "website"
urlpatterns = [
    path("", views.IndexView.as_view(), name="index"),
    path("about-us/", views.AboutView.as_view(), name="about"),
    path("contact-us/", views.ContactUsView.as_view(), name="contact_us"),
    path("newsletter/", views.NewsletterView.as_view(), name="newsletter"),
]
