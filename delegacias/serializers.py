from django.urls import path, include
from rest_framework import serializers
from .models import Delegacia

# Serializers define the API representation.
class DelegaciaSerializer(serializers.ModelSerializer):
    class Meta:
        model = Delegacia
        fields = ['localizacao', 'titulo', 'url']
