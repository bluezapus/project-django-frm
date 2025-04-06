from django.contrib.auth.forms import UserCreationForm, UserChangeForm
from . models import User

class UpdateUserForm(UserChangeForm):
    class Meta:
        model = User
        fields = [
            'name', 'email', 'birthplace', 'birth', 'phone',  'img_user',
        ]

class RegisterUserForms(UserCreationForm):
    class Meta:
        model = User
        fields = [
            'name', 'phone', 'email', 'password1', 'password2',
        ]
         
    