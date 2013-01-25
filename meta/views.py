# Create your views here.
from django.http import HttpResponse
from .models import Rooms, Users
import operator


def index(request):
    rooms = Rooms.objects.all()
    users = Users.objects.all()
    rooms_ = map(operator.attrgetter('department'), rooms)
    users_ = map(operator.attrgetter('name'), users)

    response = [",".join(rooms_), '<br>', ",".join(users_)]
    return HttpResponse("".join(response))
