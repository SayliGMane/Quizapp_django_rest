from django.shortcuts import render
from rest_framework.decorators import api_view,permission_classes,authentication_classes
from apps.questions.models import Question
from apps.questions.serializers import QuestionSerializer
from rest_framework.response import Response
from rest_framework import status
import random
from django.shortcuts import get_object_or_404
from rest_framework.permissions import IsAuthenticated
from rest_framework.authentication import BasicAuthentication,TokenAuthentication
#Create your views here.


@api_view(['GET'])
def display_questions_by_level(request, level, topic):
    # ORM fetch data from table
    list_questions = Question.objects.filter(select_level=level, select_topic=topic)
    
    # Serializer to convert queryset to JSON
    data = QuestionSerializer(list_questions, many=True)
    
    return Response(data.data, status=status.HTTP_200_OK)
# #ORM
# list_questions = list[Question.objects.filter(select_level=level,select_topic=topic)]
# #Serialiser
# random.shuffle(list_questions) 
# list_questions=list_questions[0:10]
# data = QuestionSerializer(data=list_questions, many=True)
# data.is_valid()
# #Retun
# return Response(data.data, status=status.HTTP_200_OK)
#http://127.0.0.1:8000/api/v1/questions/level/01/topic/DTV

@api_view(['POST'])
@permission_classes([IsAuthenticated])
def create_question(request):
    data = request.data
    serializer = QuestionSerializer(data=data)

    if serializer.is_valid():
        serializer.save()
        return Response(serializer.data,status=status.HTTP_201_CREATED)
    return Response(serializer.errors,status=status.HTTP_400_BAD_REQUEST)

# {
# "id": "OOP01001",
# "question": "What is the core concept of object-oriented programming (OOP)?",
# "select_level": "1",
# "select_topic": "OOP",
# "correct_answer": ["Objects and classes"],
# "incorrect_answer": ["Data structures", "Algorithms", "Functions"],
# "hint": ["Test"],
# "score": 5
#}

#242ebe3b906d639539c5d45014bbf7f0509be117


@api_view(['DELETE'])
@permission_classes([IsAuthenticated])
def delete_question(request,id):
    question= Question.objects.get(id=id)
    if question :
        question.delete()
        return Response(f"Question : {id} is deleted",status=status.HTTP_200_OK) 
    return Response({"detail": "Question not found."},status=status.HTTP_404_NOT_FOUND) 


