from django.shortcuts import render
from rest_framework.decorators import api_view
from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
import random
#Create your views here.

@api_view(['GET'])
def display_questions_by_level(request,level,topic):
   
    #ORM
    list_questions = Question.objects.filter(select_level=level,select_topic=topic)[:10]
    #Serialiser
    data = QuestionSerializer(data=list_questions, many=True)
    data.is_valid()
    #Retun
    return Response(data.data, status=status.HTTP_200_OK)



