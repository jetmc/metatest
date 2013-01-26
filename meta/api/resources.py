from tastypie.resources import ModelResource


from meta.models import Rooms, Users

from tastypie.authentication import Authentication
from tastypie.authorization import Authorization


class SillyAuthentication(Authentication):
    def is_authenticated(self, request, **kwargs):
        return True


class SillyAuthorization(Authorization):
    def is_authorized(self, request, object=None):
            return True


class RoomsResource(ModelResource):
    class Meta:
        queryset = Rooms.objects.all()
        list_allowed_methods = ['get', 'post', 'delete', 'put']
        details_allowed_methods = ['get']
        always_return_data = True
        include_resource_uri = False
        authorization = SillyAuthorization()

    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]


class UsersResource(ModelResource):
    class Meta:
        queryset = Users.objects.all()
        list_allowed_methods = ['get', 'post', 'delete', 'put']
        details_allowed_methods = ['get']
        always_return_data = True
        include_resource_uri = False
        authorization = SillyAuthorization()

    def alter_list_data_to_serialize(self, request, data):
        return data["objects"]

    def dehydrate(self, bundle):
        bundle.data['date_joined'] = bundle.data['date_joined'].strftime(
            "%m/%d/%Y"
        )
        return bundle
