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

      def validate_id(self, id):  # Correct the method name to 'validate_id'
            
            pattern = r'^(DTV|CF|F&M|DS|FL|EE|ADS|OOP)(01|02|03)\d{1,3}$'
            if re.search(pattern, id): 
                  return id
            else:
                  raise serializers.ValidationError("Invalid question id")
                  
