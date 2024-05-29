from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.dashboard.permissions import HasAdminAccessPermission


class AdminDashboardHomeView(LoginRequiredMixin, HasAdminAccessPermission, TemplateView):
    template_name = "dashboard/admin/home.html"
