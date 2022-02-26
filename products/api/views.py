from django.shortcuts import render

# Create your views here.
from rest_framework import status, viewsets
from rest_framework.decorators import action
from rest_framework.response import Response
from rest_framework import permissions

from ..models import Product

from .serializers import ProductSerializer



class ProducViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    permission_classes = [permissions.AllowAny]

    # def get_queryset(self):
    #     return self.request.user.accounts.all()