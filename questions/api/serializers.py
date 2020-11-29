from django.db import models
from rest_framework import serializers
from questions.models import Question,Answer

class AnswerSerializer(serializers.ModelSerializer):
    author          = serializers.StringRelatedField(read_only=True)
    created_at      = serializers.SerializerMethodField()

    likes_count     = serializers.SerializerMethodField()
    user_has_voted  = serializers.SerializerMethodField()
    
    class Meta:
        model = Answer
        exclude = ('questions','voters','updated_at',)

    def get_created_at(self,instance):
        return instance.created_at.strftime("%B %d  %Y")
    
    def get_likes_count(self,instance):
        return instance.voters.count()

    def get_user_has_voted(self,instance):
        request = self.context.get('request')
        return instance.voters.filter(pk = request.user.pk).exists()
    

#question serializers
class QuestionSerializer(serializers.ModelSerializer):
    author              = serializers.StringRelatedField(read_only=True)
    created_at          = serializers.SerializerMethodField(read_only=True)
    slug                = serializers.SlugField(read_only=True)
    answer_count        = serializers.SerializerMethodField(read_only=True)
    user_has_answered   = serializers.SerializerMethodField(read_only=True)

    class Meta:
        model = Question
        exclude = ['updated_at',]

    def get_created_at(self,instance):
        return instance.created_at.strftime("%B %d %Y")

    def get_answer_count(self,instance):
        return instance.answers.count()

    def get_user_has_answered(self,instance):
        request = self.context.get('request')
        return instance.answers.filter(author = request.user).exists()