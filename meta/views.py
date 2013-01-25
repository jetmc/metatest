import json

from .models import Rooms, Users

from django.http import HttpResponse
from django.views.generic.base import TemplateView
from django.views.generic.edit import CreateView
from django.views.generic.detail import SingleObjectTemplateResponseMixin


class IndexView(TemplateView):
    template_name = 'index.html'
