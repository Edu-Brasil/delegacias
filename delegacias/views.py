from django.shortcuts import render
from rest_framework import viewsets
from .models import Delegacia
from .serializers import DelegaciaSerializer


class DelegaciaViewSet(viewsets.ModelViewSet):
    queryset = Delegacia.objects.all()
    serializer_class = DelegaciaSerializer

