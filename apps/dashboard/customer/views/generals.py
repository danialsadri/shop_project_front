from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic import TemplateView
from apps.dashboard.permissions import HasCustomerAccessPermission


class CustomerDashboardHomeView(LoginRequiredMixin, HasCustomerAccessPermission, TemplateView):
    template_name = "dashboard/customer/home.html"
