from django.urls import path
from django.urls.conf import include
from rest_framework.routers import DefaultRouter
from questions.api.views import (QuestionViewSet,AnswerCreateAPIView,
                                    QuestionAnswerListAPIView,AnswerRUDAPIView,AnswerLikeAPIView,)


router = DefaultRouter()
router.register(r'questions',QuestionViewSet)


urlpatterns = [
    path('',include(router.urls)),
    path('questions/<slug:slug>/answer/list/',QuestionAnswerListAPIView.as_view(),name='answer-list'),
    path('questions/<slug:slug>/answer/',AnswerCreateAPIView.as_view(),name='answer'),
    path('answer/<int:pk>/',AnswerRUDAPIView.as_view(),name='answer-detail'),
    path('answer/<int:pk>/like/',AnswerLikeAPIView.as_view(),name='answer-like'),
]