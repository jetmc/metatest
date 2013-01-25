from tastypie.resources import ModelResource

from meta.models import Rooms, Users


class RoomsResource(ModelResource):
    class Meta:
        queryset = Rooms.objects.all()
        list_allowed_methods = ['get', 'post']
        details_allowed_methods = ['get']


class UsersResource(ModelResource):
    class Meta:
        queryset = Users.objects.all()
        list_allowed_methods = ['get', 'post']
        details_allowed_methods = ['get']
