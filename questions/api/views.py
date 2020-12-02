from django.http import request
from rest_framework import viewsets,generics,status
from rest_framework import serializers
from rest_framework.generics import get_object_or_404
from rest_framework.exceptions import ValidationError
from rest_framework.views import APIView
from rest_framework.response import Response

from questions.api.serializers import QuestionSerializer,AnswerSerializer
from questions.models import Question,Answer
from questions.api.permissions import IsAuthOrReadOnly


from rest_framework.permissions import IsAuthenticated, IsAuthenticatedOrReadOnly


#For Question
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all().order_by('-created_at')
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)



#For answer
class AnswerCreateAPIView(generics.CreateAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def perform_create(self, serializer):
        request_user  = self.request.user
        kwarg_slug = self.kwargs.get('slug')
        question  = get_object_or_404(Question,slug =kwarg_slug)

        if question.answers.filter(author = request_user).exists():
            raise ValidationError('You have already answer the questions!!')
        serializer.save(author= request_user, question= question)


#list answer question
class QuestionAnswerListAPIView(generics.ListAPIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def get_queryset(self):
        kwarg_slug = self.kwargs.get('slug')
        return Answer.objects.filter(question__slug = kwarg_slug).order_by('-created_at')
        

### Detail and Like
class AnswerRUDAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Answer.objects.all()
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated,IsAuthOrReadOnly]


#like api
class AnswerLikeAPIView(APIView):
    serializer_class = AnswerSerializer
    permission_classes = [IsAuthenticated]

    def delete(self,request,pk):
        answer = get_object_or_404(Answer,pk=pk)
        user = request.user
        answer.voters.remove(user)
        answer.save()

        serializer_context = {'request':request}
        serializer = self.serializer_class(answer,context = serializer_context)

        return Response(serializer.data,status=status.HTTP_200_OK)


    def post(self,request,pk):
        answer = get_object_or_404(Answer,pk=pk)
        user = request.user
        answer.voters.add(user)
        answer.save()

        serializer_context = {'request':request}
        serializer = self.serializer_class(answer,context = serializer_context)

        return Response(serializer.data,status=status.HTTP_200_OK)