from rest_framework import serializers
from . models import cultivo

class cultivoserializers (serializers.ModelSerializer):
    class Meta: 
        model = cultivo
        fields = ['tipo' , 'Fecha_siembra','fecha_cosecha','nombre_terreno']


       