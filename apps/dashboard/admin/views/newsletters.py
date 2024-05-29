from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core import exceptions
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, DeleteView
from apps.dashboard.permissions import *
from apps.website.models import NewsLetter


class NewsletterListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    title = "لیست خبرنامه"
    template_name = "dashboard/admin/newsletters/newsletter-list.html"
    paginate_by = 10
    ordering = "-created_date"

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        queryset = NewsLetter.objects.all().order_by("-created_date")
        search_query = self.request.GET.get('q', None)
        ordering_query = self.request.GET.get('ordering', None)
        if search_query:
            queryset = queryset.filter(
                Q(email__icontains=search_query)
            )
        if ordering_query:
            try:
                queryset = queryset.order_by(ordering_query)
            except exceptions.FieldError:
                pass
        return queryset

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["total_result"] = self.get_queryset().count()
        return context


class NewsletterDeleteView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    title = "حذف خبرنامه"
    template_name = "dashboard/admin/newsletters/newsletter-delete.html"
    success_url = reverse_lazy("dashboard:admin:newsletter-list")
    success_message = "عضو مورد نظر با موفقیت حذف شد"

    def get_queryset(self):
        return NewsLetter.objects.all()
