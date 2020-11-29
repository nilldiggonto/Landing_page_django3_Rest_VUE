from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from questions.api.views import QuestionViewSet


router = DefaultRouter()
router.register(r'questions',QuestionViewSet)


urlpatterns = [
    path('',include(router.urls)),
]