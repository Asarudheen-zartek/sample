from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from ..models import User

from .serializers import UserSerializer, LoginSerializer

from rest_framework.views import APIView
from rest_framework import generics


class ProfileAPIView(APIView):

    def get(self, request, **kwargs):
        user = request.user
        serilaizer = UserSerializer(user)
        return Response({"data":serilaizer.data},status=200)



class LoginAPIView(generics.GenericAPIView):

    serializer_class = LoginSerializer

    def post(self, request, *args, **kwargs):
        serializer = self.serializer_class(data=request.data)
        if serializer.is_valid():
            return Response(serializer.data,status=200)
        return Response(serializer.errors,status=200)

