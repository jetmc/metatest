from tastypie.api import Api
from resources import UsersResource, RoomsResource

v1 = Api('v1')
v1.register(UsersResource())
v1.register(RoomsResource())
