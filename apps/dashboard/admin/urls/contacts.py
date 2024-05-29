from django.urls import path
from .. import views

urlpatterns = [
    path("contact/list/", views.ContactListView.as_view(), name="contact-list"),
    path("contact/<int:pk>/detail/", views.ContactDetailView.as_view(), name="contact-detail"),
]
