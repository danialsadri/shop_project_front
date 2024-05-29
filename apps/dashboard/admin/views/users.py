from django.contrib.auth.mixins import LoginRequiredMixin
from django.contrib.messages.views import SuccessMessageMixin
from django.core import exceptions
from django.db.models import Q
from django.urls import reverse_lazy
from django.views.generic import ListView, UpdateView, DeleteView
from apps.dashboard.admin.forms import *
from apps.dashboard.permissions import *

User = get_user_model()


class UserListView(LoginRequiredMixin, HasAdminAccessPermission, ListView):
    title = "لیست کاربران"
    template_name = "dashboard/admin/users/user-list.html"
    paginate_by = 10
    ordering = "-created_date"

    def get_paginate_by(self, queryset):
        return self.request.GET.get('paginate_by', self.paginate_by)

    def get_queryset(self):
        queryset = User.objects.filter(is_superuser=False, type=UserType.customer.value).order_by("-created_date")
        search_query = self.request.GET.get('q', None)
        ordering_query = self.request.GET.get('ordering', None)
        if search_query:
            queryset = queryset.filter(Q(email__icontains=search_query))
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


class UserDeleteView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, DeleteView):
    title = "حذف کاربر"
    template_name = "dashboard/admin/users/user-delete.html"
    success_url = reverse_lazy("dashboard:admin:user-list")
    success_message = "کاربر مورد نظر با موفقیت حذف شد"

    def get_queryset(self):
        return User.objects.filter(is_superuser=False, type=UserType.customer.value)


class UserUpdateView(LoginRequiredMixin, HasAdminAccessPermission, SuccessMessageMixin, UpdateView):
    title = "ویرایش کاربر"
    template_name = "dashboard/admin/users/user-edit.html"
    success_message = "کاربر مورد نظر با موفقیت ویرایش شد"
    form_class = UserForm

    def get_success_url(self) -> str:
        return reverse_lazy("dashboard:admin:user-edit", kwargs={"pk": self.kwargs.get("pk")})

    def get_queryset(self):
        return User.objects.filter(is_superuser=False, type=UserType.customer.value)
