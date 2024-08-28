from rest_framework import serializers
from apps.questions.models import Question  
import re


# class CreateQuestionSerializer(serializers.ModelSerializer):
#     class Meta:
#             model = Question
#             fields = "__all__" 



class QuestionSerializer(serializers.ModelSerializer):
    class Meta:
            model = Question
            fields = "__all__" 

    def validate_question_id(self,id):   
          if re.search(r'(DTV|CF|F&M|DS|FL|EE|ADS|OOP)(01|02|03)\d{1,3}',id):
                return id
          else:
                raise serializers.ValidationError("Invalid question id")
               
