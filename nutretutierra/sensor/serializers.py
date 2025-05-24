from rest_framework import serializers
from .models import sensor

class sensroseralizado (serializers.ModelSerializer):

    model = sensor

    fields = ['id','descripcion','ubicacion','fecha_instal']