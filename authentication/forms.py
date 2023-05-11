from django.contrib.auth.forms import UserCreationForm
from django.utils.translation import gettext_lazy as _
from authentication.models import CustomUser
class CustomUserCreationForm(UserCreationForm):

    class Meta(UserCreationForm.Meta):
        model = CustomUser
        fields = ('username', 'email', 'password1', 'password2')
        error_messages = {
            "email": {
                "unique": _("A user with that Email already exists."),
            },
             "username": {
                "unique": _("A user with that username already exists."),
            },
        }
