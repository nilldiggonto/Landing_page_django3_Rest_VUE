from rest_framework import viewsets
from questions.api.serializers import QuestionSerializer
from questions.models import Question
from questions.api.permissions import IsAuthOrReadOnly
from rest_framework.permissions import IsAuthenticated
class QuestionViewSet(viewsets.ModelViewSet):
    queryset = Question.objects.all()
    lookup_field = 'slug'
    serializer_class = QuestionSerializer
    permission_classes = [IsAuthenticated, IsAuthOrReadOnly]

    def perform_create(self, serializer):
        serializer.save(author = self.request.user)

