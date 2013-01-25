from django.contrib import admin
from .models import Rooms, Users


class RoomsAdmin(admin.ModelAdmin):
    pass


class UsersAdmin(admin.ModelAdmin):
    pass


admin.site.register(Rooms, RoomsAdmin)
admin.site.register(Users, UsersAdmin)
