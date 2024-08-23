from rest_framework import serializers
from apps.questions.models import Question  


# class CreateQuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#             model = Question
#             fields = "__all__" 



class ReadQuestionSerializer(serializers.ModelSerializer):
    class Meta:
            model = Question
            fields = "__all__" 
