from django.urls import path
from .. import views

urlpatterns = [
    path("newsletter/list/", views.NewsletterListView.as_view(), name="newsletter-list"),
    path("newsletter/<int:pk>/delete/", views.NewsletterDeleteView.as_view(), name="newsletter-delete"),
]
