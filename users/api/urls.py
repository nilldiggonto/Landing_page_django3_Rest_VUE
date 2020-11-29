from django.urls import path
from django.urls.resolvers import URLPattern
# from users.api.serializers import UserDisplaySerializer
from users.api.views import CurrentUserAPIView
from django.urls import path

urlpatterns = [
    path('user/',CurrentUserAPIView.as_view(),name='current_user'),

]