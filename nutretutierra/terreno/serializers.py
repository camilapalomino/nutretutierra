from rest_framework import serializers
from .models import terreno

class terrenoserializers (serializers.ModelSerializer):
    class Meta:
        model = terreno
        fields = [ 'propietario', 'nombre','ubicación', 'tamaño']