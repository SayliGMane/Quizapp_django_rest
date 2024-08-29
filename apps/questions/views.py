from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes
from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
import random
from rest_framework.permissions import IsAuthenticated
#Create your views here.

@api_view(['GET'])
def display_questions_by_level(request,level,topic):
   
    #ORM
    list_questions = list[Question.objects.filter(select_level=level,select_topic=topic)]
    #Serialiser
    random.shuffle(list_questions) 
    list_questions=list_questions[0:10]
    data = QuestionSerializer(data=list_questions, many=True)
    data.is_valid()
    #Retun
    return Response(data.data, status=status.HTTP_200_OK)



# @api_view(['POST'])
# @permission_classes([IsAuthenticated])
# def create_question(request):
#     data = request.data
#     serializer = QuestionSerializer(data=data)

#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data,status=status.HTTP_201_CREATED)
#     else: 
#         #print("problem")
#         return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)


# data = '{
#     "id": "OOP01001",
#     "question": "What is the core concept of object-oriented programming (OOP)?",
#     "select_level": "1",
#     "select_topic": "OOP",
#     "correct_answer": ["Objects and classes"],
#     "incorrect_answer": ["Data structures", "Algorithms", "Functions"],
#     "hint": ["Test"],
#     "score": 5
# }'