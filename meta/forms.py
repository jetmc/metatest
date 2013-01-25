from djang import forms
from .models import Rooms, Users


class RoomsForm(forms.ModelForm):
    class Meta:
        model = Rooms


class UsersForm(forms.ModelForm):
    class Meta:
        model = Users
