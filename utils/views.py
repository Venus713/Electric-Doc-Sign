from django.utils.translation import gettext_lazy as _
from django.views.generic import TemplateView
from rest_framework import status
from rest_framework.response import Response
from rest_framework.renderers import JSONRenderer
from rest_framework.viewsets import ModelViewSet


class HomePage(TemplateView):
    template_name = 'layout/index.html'
