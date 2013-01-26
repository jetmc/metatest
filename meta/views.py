from .models import Rooms, Users
from django.views.generic.base import TemplateView
import json
from datetime import date


def serialize(items, fields=()):
    result = []
    for item in items:
        item_ = {'id': item.pk}
        for field in fields:
            value = getattr(item, field)
            if isinstance(value, date):
                value = value.strftime('%m/%d/%Y')
            item_[field] = value
        result.append(item_)
    return json.dumps(result)


class IndexView(TemplateView):

    template_name = 'index.html'

    def get_context_data(self, **kwargs):
        context = super(IndexView, self).get_context_data(**kwargs)
        context['rooms'] = serialize(Rooms.objects.all(),
                                     ('department', 'spots'))
        context['users'] = serialize(Users.objects.all(),
                                     ('name', 'paycheck', 'date_joined'))
        return context
