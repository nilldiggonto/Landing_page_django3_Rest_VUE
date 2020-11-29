
from django.contrib import admin
from django.urls import path,include

from users.forms import CustomUserForm
from django_registration.backends.one_step.views import RegistrationView

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounts/',include('django_registration.backends.one_step.urls')),

    path('accounts/registration/',RegistrationView.as_view(form_class=CustomUserForm, success_url='/'),
                                        name = 'django_registration_register'),

    

    path('api-auth/',include('rest_framework.urls')),
    path('api/rest-auth/',include('rest_auth.urls')),

    path('api/rest-auth/registration/',include('rest_auth.registration.urls')),
]
