from django_registration.forms import RegistrationForm
from ask.users.models import CustomUser

class CustomUserForm(RegistrationForm):
    class Meta(RegistrationForm.Meta):
        model = CustomUser