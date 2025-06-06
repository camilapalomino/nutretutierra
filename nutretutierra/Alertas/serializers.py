from rest_framework import serializers
from .models import configuracionalerta

class alertaserializers(serializers.ModelSerializer):
    class Meta:
        model = configuracionalerta
        fields = ['humedad_minima', 'humedad_maxima', 'ultima_actualizacion']