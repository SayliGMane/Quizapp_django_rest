from django.shortcuts import render
from rest_framework.decorators import api_view, permission_classes, authentication_classes
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response
from rest_framework import status
from django.contrib.auth.models import User
from apps.user.serializer import UserSerializer
# Create your views here.

@api_view(['GET'])
@permission_classes([IsAuthenticated])
def user_profile(request, ids):

    user = User.objects.filter(id=ids)

    data = UserSerializer(user)

    return Response(data.data, status=status.HTTP_200_OK)