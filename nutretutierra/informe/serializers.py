from rest_framework import serializers

from .models import informe

class informeserializers (serializers.models):
    class Meta:
        model = informe
        fields = ['titulo' , 'informacion' , 'generacion' , 'alerta']

        

