from django.contrib.auth.mixins import LoginRequiredMixin
from django.views.generic.base import TemplateView
from rest_framework.permissions import IsAuthenticated

class IndexTemplateView(LoginRequiredMixin, TemplateView):

    template_name = "index.html"